import win32com.client
import pythoncom
import sys

class XASessionReceiver:
    """
    이 클래스는 XASession에서 서버에 요청한 내용의 결과값을 수신 받는 역할을 한다.
    """
    def __init__(self):
        self.parent = None

    def OnLogin(self, code, msg):
        """
        로그인이 성공적으로 서버로 전송이 되면 로그인에 대한 결과값은 Login 이벤트로 들어오게 됩니다.
        현재 self.parent에는 XASession 인스턴스가 할당되었기 때문에, XASession의 변수에 접근할 수 있게 되었다.
        """
        if code == "0000":
            print("로그인에 성공했습니다.")
            self.parent.response = True
        else:
            print(f"로그인 실패: {code} | {msg}")
            sys.exit()  # 시스템 강제 종료

    def OnDisconnect(self):
        """ 인터넷 등의 영향이나 이상현상으로 불가피하게 서버와의 연결이 끊겼을 때 실행되는 함수 """
        print("서버와의 연결이 끊겼습니다.")
        sys.exit()  # 시스템 강제 종료

class XASession:
    """ 
    로그인, 계좌정보를 가지고 오는 클래스 
    - self.login_server : main 함수에서 인수에 값으로 받아서 서버 주소를 설정한다.
    - self.session : win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver) 함수를 통해서 XASessionReceiver의 이벤트가 되었다.
    - self.sesssion.ConnectServer(self.login_server) : 서버에 연결하는 함수.
    """

    def __init__(self, login_server):
        self.login_server = self.set_server(login_server=login_server)
        self.sesssion = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver)

        # login() 함수에서 로그인이 성공하면 이 값을 True로 변경하여 다음 코드로 진행할 수 있도록 한다.
        self.response = False 

        # XASessionReceiver의 self.parent 변수에 접근하여 XASession의 self 값을 전달하여,
        # XASessionReceiver에서 XASession에 접근할 수 있도록 한다.
        self.sesssion.parent = self

    @staticmethod
    def set_server(login_server):
        """ 서버 주소 선택 """
        if login_server == "실투자":
            return "api.ls-sec.co.kr"
        elif login_server == "모의투자":
            return "demo.ls-sec.co.kr"
        elif login_server == "가상거래소":
            return "127.0.0.1"

    def connect_server(self):
        """ 서버 연결하기 """
        res = self.sesssion.ConnectServer(self.login_server, 20001) # res : True/False
        
        if not res:
            error_code = self.sesssion.GetLastError()
            error_msg = self.sesssion.GetErrorMessage(error_code)
            print(error_msg)
            sys.exit()  # 시스템 강제 종료

    def disconnect_server(self):
        self.sesssion.DisconnectServer()
        sys.exit()  # 시스템 강제 종료

    def disconnect_server2(self):
        # 서버와의 연결을 끊어야 하는 경우 이 함수를 사용하면 된다.
        self.sesssion.DisconnectServer()

    def login(self, crypto_wallet):
        """ 로그인을 요청한 후에는 실제로 로그인이 될 때까지 다음 코드를 실행하지 않고 기다려야 한다. """
        _id = crypto_wallet["id"]
        _pw = crypto_wallet["pwd"]
        _cert = crypto_wallet["cert_pwd"]
        _acc_pw = crypto_wallet["acc_pwd"]

        self.sesssion.Login(_id, _pw, _cert, 0, False)

        # response 값이 false이면, 즉 로그인 아직 안되어 있으면 계속해서 기다린다.
        # 로그인이 성공했으면, XASessionReceiver의 OnLogin 함수에서 response를 True로 만들어서 아래 루프를 종료한다.
        while not self.response:
            pythoncom.PumpWaitingMessages()

    def get_account_list(self):
        """ page 11 : 계좌 가져오기 """
        # 1) 계좌 개수 가져오기
        cnt = self.sesssion.GetAccountListCount()
        account_list = list()
        # 2) 계좌 개수만큼 계좌번호 읽어들여서 account_list 에 추가하기기
        for idx in range(cnt):
            account_num = self.sesssion.GetAccountList(idx)
            account_list.append(account_num)

        return account_list