from src.config.menulist import *
import win32com.client
import pythoncom
import queue
import inspect



class XARealReceiver:
    def __init__(self):
        self.parent = None

    def OnReceiveRealData(self, tr_code):
        # 실시간 체결
        if tr_code == "S3_": # KOSPI 실시간 체결
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["KOSPI체결"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["KOSPI체결", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "UH1": # (통합) 호가 잔량
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["(통합)호가잔량"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["(통합)호가잔량", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "US2": # (통합)우선호가
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["(통합)우선호가"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["(통합)우선호가", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "US3": # (통합)체결
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["(통합)체결"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["(통합)체결", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "H1_": # KOSPI 호가 잔량
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["KOSPI호가잔량"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["KOSPI호가잔량", dict(zip(OUT_BLOCK_NAME, item))])

        if tr_code == "K3_": # KOSDAQ 실시간 체결
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["KOSDAQ체결"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["KOSDAQ체결", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "HA_": # KOSDAQ 호가 잔량
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["KOSDAQ호가잔량"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["KOSDAQ호가잔량", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "I5_": # 코스피 ETF 종목 실시간 NAV
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["코스피ETF종목실시간NAV"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["코스피ETF종목실시간NAV", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "VI_": # 주식 VI 발동/해제
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["VI"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["VI", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code == "SC0": # 주식 주문접수
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict["주문접수"].GetFieldData("OutBlock", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            self.parent.queue.put(["주문접수", dict(zip(OUT_BLOCK_NAME, item))])

        elif tr_code in ["SC1", "SC2", "SC3", "SC4"]:
            if tr_code == "SC1":
                tr_code_type = "주문체결"
            if tr_code == "SC2":
                tr_code_type = "주문정정"
            if tr_code == "SC3":
                tr_code_type = "주문취소"
            if tr_code == "SC4":
                tr_code_type = "주문거부"
            
            item = list()
            for idx in range(len(SCN_OUT_BLOCK_CODE)):
                out_block_code = SCN_OUT_BLOCK_CODE[idx]
                data = self.parent.real_dict[tr_code_type].GetFieldData("OutBlock", out_block_code)
                item.append(data)

            self.parent.queue.put([tr_code_type, dict(zip(SCN_OUT_BLOCK_NAME, item))])


class XAReal:
    # def __init__(self, account_dict, outstanding_list, deposit):
    def __init__(self):
        self.response = False
        
        # (1) XRealReceiver의 여러 인스턴스들 생성
        self.real_dict = self.real_objects()
        self.queue = queue.Queue()
        self.real_registered = {tr: set() for tr in self.real_dict.keys()}

        # self.account_dict = account_dict
        # self.outstanding_list = outstanding_list
        # self.deposit = deposit

        # res file들이 저장된 곳.
        self.resFile_url = "C:/LS_SEC/xingAPI/Res/"


    def real_objects(self):
        item = dict()
        headers = [
            "(통합)체결", "(통합)호가잔량", "(통합)우선호가", "KOSPI호가잔량", "KOSDAQ호가잔량", "코스피ETF종목실시간NAV", "지수", 
            "KOSDAQ체결", "KOSDAQ우선호가", "KOSPI우선호가", "KOSPI체결", "주문접수", "주문체결", "주문정정", "주문취소", "주문거부", "VI" 
        ]
        for header in headers:
            # (1) XARealReceiver 인스턴스 생성.
            real = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", XARealReceiver)
            real.parent = self
            item[header] = real

        return item
       
    def S3_(self, shcode):
      # [수정]
        tr_code = "S3_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["KOSPI체결"]

        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       

        # 현재 함수의 인수 목록 가져오기
        # arg_names = inspect.signature(self.S3_).parameters.keys()
        # for arg in arg_names:
        #     if arg not in ["self"]:
        #         arg_name = arg
        # real.SetFieldData("InBlock", arg_name, shcode) 
        real.SetFieldData("InBlock", "shcode", shcode)
        # 실시간 데이터 요청
        real.AdviseRealData()

    def UH1(self, shcode):
      # [수정]
        tr_code = "UH1"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["(통합)호가잔량"]

        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "ex_shcode", f"U{shcode}")
        # 실시간 데이터 요청
        real.AdviseRealData()
        self.real_registered["(통합)호가잔량"].add(f"U{shcode}")

    def unadvise_all(self):
        """
        실시간 등록된 모든 XAReal 인스턴스의 실시간 데이터를 모두 해제합니다.
        """
        for tr_name, real in self.real_dict.items():
            try:
                real.UnadviseRealData()
            except Exception as e:
                print(f"[{tr_name}] 전체 해제 실패: {e}")        

    def unadvise_by_tr_and_code(self, tr_name, shcode):
        """
        특정 실시간TR에 특정 종목만 해제
        :param tr_name: 예) '(통합)호가잔량', 'KOSPI체결', '주문접수' 등
        :param shcode: 종목코드 (필요시 앞에 U, A 등 prefix 붙여줘야 함)
        """
        if tr_name not in self.real_dict:
            print(f"TR명 {tr_name}은 등록된 실시간 객체가 아닙니다.")
            return

        real = self.real_dict[tr_name]
        # (통합)호가잔량인 경우 prefix 'U'가 붙으니, 미리 확인
        key = shcode
        if tr_name == "(통합)호가잔량" and not shcode.startswith("U"):
            key = f"U{shcode}"

        try:
            real.UnadviseRealDataWithKey(key)
            self.real_registered[f"{tr_name}"].discard(key)
            print(f"{tr_name} - {key} 해제 완료")
        except Exception as e:
            print(f"{tr_name} - {key} 해제 실패: {e}")

    def show_registered(self, tr_name=None):
        if tr_name:
            codes = self.real_registered.get(tr_name, set())
            print(f"{tr_name} 등록종목: {sorted(codes)}")
            return codes
        else:
            for tr, codes in self.real_registered.items():
                if codes:
                    print(f"{tr}: {sorted(codes)}")

    def US2(self, shcode):
      # [수정]
        tr_code = "US2"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["(통합)우선호가"]

        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "ex_shcode", f"U{shcode}")
        # 실시간 데이터 요청
        real.AdviseRealData()

    def US3(self, shcode):
      # [수정]
        tr_code = "US3"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["(통합)체결"]

        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "ex_shcode", f"U{shcode}")
        # 실시간 데이터 요청
        real.AdviseRealData()

    def K3_(self, shcode):
      # [수정]
        tr_code = "K3_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["KOSDAQ체결"]

        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "shcode", shcode)
        # 실시간 데이터 요청
        real.AdviseRealData()

    def H1_(self, shcode):
      # [수정]
        tr_code = "H1_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["KOSPI호가잔량"]
        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "shcode", shcode)
        # (3) 실시간 데이터 요청
        real.AdviseRealData()

    def HA_(self, shcode):
      # [수정]
        tr_code = "HA_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["KOSDAQ호가잔량"]
        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "shcode", shcode)
        # (3) 실시간 데이터 요청
        real.AdviseRealData()

    def I5_(self, shcode):
      # [수정]
        tr_code = "I5_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["코스피ETF종목실시간NAV"]
        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "shcode", shcode)
        # (3) 실시간 데이터 요청
        real.AdviseRealData()

    def VI_(self, shcode):
      # [수정]
        tr_code = "VI_"  
        # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
        real = self.real_dict["VI"]
        # (2) RES 등록.
        real.ResFileName = f"{self.resFile_url}{tr_code}.res"       
        real.SetFieldData("InBlock", "shcode", shcode)
        # (3) 실시간 데이터 요청
        real.AdviseRealData()

    def SCN(self):
        """
        주식주문 관련 일괄 등록
        SC0 : 주식주문접수
        SC1 : 주식주문체결
        SC2 : 주식주문정정
        SC3 : 주식주문취소
        SC4 : 주식주문거부
        """
        headers = ["주문접수", "주문체결", "주문정정", "주문취소", "주문거부"]
        for idx in range(len(headers)):
            # (1) XRealReceiver의 여러 인스턴스들 중에서 해당 인스턴스를 선택
            real = self.real_dict[headers[idx]]
            # (2) RES 등록.
            real.ResFileName = f"{self.resFile_url}SC{idx}.res"       
            # (3) 실시간 데이터 요청
            real.AdviseRealData()
