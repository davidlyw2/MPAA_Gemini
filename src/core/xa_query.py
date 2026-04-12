from src.config.menulist import *
import win32com.client
import pythoncom
import sys
import time
import inspect
import queue
from collections import defaultdict, deque
import pandas as pd

class XAQueryReceiver:
    """
    이 클래스는 XAQuery에서 서버에 요청한 내용의 결과값을 수신 받는 역할을 한다.
    """
    def __init__(self):
        self.account_num = None
        self.password = None
        self.parent = None
        self.datas = [] # 연속조회를 할 경우에 함수에 넣을 인자들 값.
        # self.conn = sqlite3.connect('data.db')
        self.t8410_count_receiver = 0

    def OnReceiveMessage(self, bIsSystemError, code, msg):
        """ 데이터를 요청했을 때, 처리 결과 메시지를 수신하는 함수 """
        self.parent.last_msg_is_system_error = bIsSystemError
        self.parent.last_msg_code = str(code).strip()
        self.parent.last_msg_text = str(msg).strip()
        if bIsSystemError != 0:
            print(f"    *****OnReceiveMessage: {bIsSystemError} | {code} | {msg}")
        self.parent.response = True

    def OnReceiveData(self, tr_code):
        """ 요청한 데이터 자체를 수신받는 함수 """
        # print(f"    ***** Event ([{TR_LIST[tr_code]}][{tr_code}]) Received ...")

        if tr_code == "CSPAQ12300":   # 현물계좌 잔고내역 조회
            account_dict = dict()

            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]
            OUT_BLOCK_2_CODE = OUT_BLOCK[2]
            OUT_BLOCK_2_NAME = OUT_BLOCK[3]
            OUT_BLOCK_3_CODE = OUT_BLOCK[4]
            OUT_BLOCK_3_NAME = OUT_BLOCK[5]

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock3")

            # 디버깅 중 남은 blocking 입력 제거: 실운영에서는 즉시 다음 로직 진행
            # print(f">>>>> CSPAQ12300: count : {count}")

            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(OUT_BLOCK_3_CODE)):
                    out_block_code = OUT_BLOCK_3_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock3", out_block_code, cnt)
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                code = item[0]
                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                # [수정] 조회한 데이터 저장용 변수
                self.parent.account_list.append(dict(zip(OUT_BLOCK_3_NAME, item)))
                account_dict[code]  = dict(zip(OUT_BLOCK_3_NAME, item))
            self.parent.account_dict = account_dict
            # [수정] --- 연속 데이터 조회
            if count == 20: # 한 화면에 20개씩 조회가 가능하다. 그러므로 추가로 몇개가 더 있을 지 확인할 수 있는 방법이 현재로서는 이 개수로 확인한다.
                self.parent.request_balance(account_num=self.datas[1], password=self.datas[2], cont=True)

        elif tr_code == "CSPAQ13700":   # 현물계좌 주문체결내역 조회
            CSPAQ13700_dict = dict()

            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분.
            item = list()
            for idx in range(len(CSPAQ13700_OUT_BLOCK_2_CODE)):
                out_block_code = CSPAQ13700_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            # zip(left, right) : left와 right 데이터를 하나씩 묶어준다. dic() : dictionary 형태로 만들어 준다.
            # print(dict(zip(CSPAQ12300_OUT_BLOCK_2_NAME, item)))

            # OCCURS 특성을 갖는 블럭에서 몇 번의 데이터를 출력할 수 있는지 확인하는 코드.  이 후의 블럭을 복사해서 사용.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock3")
            for cnt in range(count):
                item = list()
                for idx in range(len(CSPAQ13700_OUT_BLOCK_3_CODE)):
                    out_block_code = CSPAQ13700_OUT_BLOCK_3_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock3", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                # zip(left, right) : left와 right 데이터를 하나씩 묶어준다. dic() : dictionary 형태로 만들어 준다.
                # print(dict(zip(CSPAQ13700_OUT_BLOCK_3_NAME, item)))      
                code = item[5]     # IsuNo : 종목번호. 이 값을 account_dictionary의 키 값으로 사용
                CSPAQ13700_dict[code]  = dict(zip(CSPAQ13700_OUT_BLOCK_3_NAME, item))
            
            self.parent.CSPAQ13700_dict = CSPAQ13700_dict

        elif tr_code == "CSPAQ22200":   # 현물계좌 예수금/주문가능금액/총평가 조회 
            deposit_dict = dict()   # 계좌잔고 정보 저장

            item = list()
            for idx in range(len(CSPAQ22200_OUT_BLOCK_2_CODE)):
                out_block_code = CSPAQ22200_OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock2", out_block_code, 0)
                # data = self.parent.query.GetFieldData("CSPAQ12200OutBlock2", out_block_code, 0)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            # zip(left, right) : left와 right 데이터를 하나씩 묶어준다. dic() : dictionary 형태로 만들어 준다.
            # print(dict(zip(CSPAQ22200_OUT_BLOCK_2_NAME, item)))
            deposit_dict = dict(zip(CSPAQ22200_OUT_BLOCK_2_NAME, item))

            self.parent.deposit_dict = deposit_dict

        elif tr_code == "t8410": # 주식 차트 (일주년월)
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))

            # [수정] 연속데이터조회용 인자
            cts_date = out_block["연속일자"]                           # print(f"주문번호 : {cts_ordno}")

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")            # print(f">>>>> t8410: count : {count}")            # input("============== ")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                # [수정] 조회한 데이터 저장용 변수
                date = item[0]     # date : 날짜. 이 값을 self.parent.chart_dict의 키 값으로 사용                # self.parent.chart_dict[date]  = dict(zip(OUT_BLOCK_1_NAME, item)) # print(f" >>> ETF 일별추이 : chart_dict")
                self.parent.chart_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))                 # print(f">>>>>> t8410 : {self.parent.chart_list}")
            
            # [수정] --- 연속 데이터 조회
            if cts_date != "":
                self.parent.t8410(shcode=self.datas[0], gubun=self.datas[1], qrycnt=self.datas[2], sdate=self.datas[3], edate=self.datas[4], cts_date=cts_date, comp_yn=self.datas[6], sujung=self.datas[7], cont=True)

        elif tr_code == "t8411": # 주식 차트 (틱/n틱) # 수정할 것.
            # chart_ntick_dict = dict()

            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            item = list()
            for idx in range(len(T8411_OUT_BLOCK_CODE)):
                out_block_code = T8411_OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(T8411_OUT_BLOCK_NAME, item))
            # print(dict(zip(T8411_OUT_BLOCK_NAME, item)))
            cts_date = out_block["연속일자"]                           # print(f"주문번호 : {cts_ordno}")
            cts_time = out_block["연속시간"]

            # OCCURS 특성을 갖는 블럭에서 몇 번의 데이터를 출력할 수 있는지 확인하는 코드.  이 후의 블럭을 복사해서 사용. : OutBlock1- OCCURS
            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(T8411_OUT_BLOCK_1_CODE)):
                    out_block_code = T8411_OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                # print(dict(zip(T8411_OUT_BLOCK_1_NAME, item)))  
                # chart_ntick_dict.append(dict(zip(T8411_OUT_BLOCK_1_NAME, item)))    
                self.parent.chart_ntick_list.append(dict(zip(T8411_OUT_BLOCK_1_NAME, item)))    
            
            # --- 연속 데이터 조회
            # time.sleep(1.1) # 한 번에 많은 조회를 하는 것을 조심해야 함.            print(f"주문번호 : {cts_ordno}")
            if cts_date != "":
                self.parent.t8411(shcode="005930", ncnt="1", qrycnt="500", sdate="", edate="당일", cts_date=cts_date, cts_time=cts_time, comp_yn="N", cont=True)

            # self.parent.chart_ntick_dict = chart_ntick_dict

        elif tr_code == "t8412": # 주식 차트 (N분)
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            cts_date = out_block["연속일자"]                           # print(f"주문번호 : {cts_ordno}")
            cts_time = out_block["연속시간"]

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                date = item[0] + item[1]     # date + time : 날짜&시간간. 이 값을 self.parent.chart_min_dict의 키 값으로 사용
                # self.parent.chart_min_dict[date]  = dict(zip(OUT_BLOCK_1_NAME, item))
                self.parent.chart_min_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))
            
            # --- 연속 데이터 조회
            time.sleep(3.3) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if cts_date != "":
                self.parent.t8412(shcode=self.datas[0], ncnt=self.datas[1], qrycnt=self.datas[2], nday=self.datas[3], sdate=self.datas[4], edate=self.datas[6], cts_date=cts_date, cts_time=cts_time, comp_yn=self.datas[10], cont=True)

        elif tr_code == "t8430": # 주식 종목 조회.
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(T8430_OUT_BLOCK_CODE)):
                    out_block_code = T8430_OUT_BLOCK_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                out_block = dict(zip(T8430_OUT_BLOCK_NAME, item))
                # print(dict(zip(T8430_OUT_BLOCK_NAME, item)))

        elif tr_code == "t8451": # 주식 차트 (일주년월)
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))

            # [수정] 연속데이터조회용 인자
            cts_date = out_block["연속일자"]                           # print(f"주문번호 : {cts_ordno}")

            # --- 반복 데이터 조회 하기.
            # self.parent.chart_dict = {}
            # self.parent.chart_list = []
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  

                # [수정] 조회한 데이터 저장용 변수
                date = item[0]     # date : 날짜. 이 값을 self.parent.chart_dict의 키 값으로 사용
                self.parent.chart_dict[date]  = dict(zip(OUT_BLOCK_1_NAME, item)) # print(f" >>> ETF 일별추이 : chart_dict")
                self.parent.chart_list.append(dict(zip(OUT_BLOCK_1_NAME, item))) 
                # df = dict(zip(OUT_BLOCK_1_NAME, item))
                # df['symbol'] = self.datas[0]
                # df = pd.DataFrame([df])
                # df.to_sql('data', self.conn, if_exists='append', index=False)
                # print(f'{self.datas[0]}: 데이터베이스에 저장 완료')
            
            # [수정] --- 연속 데이터 조회
            if cts_date != "":
                self.parent.t8451(shcode=self.datas[0], gubun=self.datas[1], qrycnt=self.datas[2], sdate=self.datas[3], edate=self.datas[4], cts_date=cts_date, comp_yn=self.datas[6], sujung=self.datas[7], exchgubun=self.datas[8], cont=True)

        elif tr_code == "t1444": # 시가총액상위 종목 조회
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))

            # [수정] 연속데이터조회용 인자
            _idx = out_block["IDX"]

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")  # 현재 창에 몇개의 데이터 리스트가 있는지
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                # [수정] 키 값에 사용할 데이터를 필요하면 수정할 것.
                key = item[0]     # shcode : 종목코드. 이 값을 self.parent.t1444_dict의 키 값으로 사용
                self.parent.t1444_dict[key]  = dict(zip(OUT_BLOCK_1_NAME, item))
            
            # --- 연속 데이터 조회
            time.sleep(1.1) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if int(_idx) <= 100:
                self.parent.t1444(upcode=self.datas[0], idx=_idx, cont=True)

        elif tr_code == "t8424": # 업종전체 조회
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock")  # 현재 창에 몇개의 데이터 리스트가 있는지
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_CODE)):
                    out_block_code = OUT_BLOCK_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_NAME, item)))
                # [수정] 해당 tr_code 이름으로 변경할 것.
                self.parent.t8424_list.append(dict(zip(OUT_BLOCK_NAME, item)))

        elif tr_code == "t1441": # 등락율상위 종목 조회
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))

            # [수정] 연속데이터조회용 인자
            _idx = out_block["IDX"]

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")  # 현재 창에 몇개의 데이터 리스트가 있는지
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                    if out_block_code == "value":
                        total_money = int(data) # 단위 백만,
                        if total_money >= 30000:    # 거래대금이 300억 이상인 종목
                            # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                            # [수정] 키 값에 사용할 데이터를 필요하면 수정할 것.
                            key = cnt #item[12]     # shcode : 종목코드. 이 값을 self.parent.t1441_dict의 키 값으로 사용
                            self.parent.t1441_dict[key]  = dict(zip(OUT_BLOCK_1_NAME, item))
                            self.parent.t1441_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))
            
            # --- 연속 데이터 조회
            # time.sleep(1.1) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if int(_idx) <= 50:
                self.parent.t1441(gubun1=self.datas[0], gubun2=self.datas[1], gubun3=self.datas[2], jc_num=self.datas[3], sprice=self.datas[4], eprice=self.datas[5], volume=self.datas[6], idx=_idx, jc_num2=self.datas[8], cont=True)            

        elif tr_code == "t1444": # 시가총액상위.
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]

            item = list()
            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block1 = dict(zip(OUT_BLOCK_1_NAME, item))
            self.parent.t1444_list.append(out_block1)
            # print(out_block1)

        elif tr_code == "t1486": # 시간대별 예상 체결가
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) 
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))

            # [수정] 연속데이터조회용 인자
            cts_time = out_block["시간CTS"][:8]            # print(f"시간CTS : {cts_time}")
            # cts_time = '085959'

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                # [수정] 조회한 데이터 저장용 변수
                date = item[0]     # date : 날짜. 이 값을 self.parent.chart_dict의 키 값으로 사용                # self.parent.chart_dict[date]  = dict(zip(OUT_BLOCK_1_NAME, item)) # print(f" >>> ETF 일별추이 : chart_dict")
                self.parent.t1486_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))                 # print(f">>>>>> t8410 : {self.parent.chart_list}")
            
            # [수정] --- 연속 데이터 조회
            if cts_time != "":
                self.parent.t1486(shcode=self.datas[0], cts_time=cts_time, cnt=self.datas[2], exchgubun=self.datas[3], cont=True)

        elif tr_code == "t0425": # 주식 체결/미체결
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            self.parent.t0425_outblock_list.append(dict(zip(OUT_BLOCK_NAME, item)))
            # [수정] 연속데이터조회용 인자
            cts_ordno = str(out_block["주문번호"])

            # --- 반복 데이터 조회 하기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")  # 현재 창에 몇개의 데이터 리스트가 있는지
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                # [수정] 키 값에 사용할 데이터를 필요하면 수정할 것.
                # key = item[0]     # ordno : 주문번호. 이 값을 self.parent.t0425_dict의 키 값으로 사용
                self.parent.t0425_outblock1_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))
            
            # --- 연속 데이터 조회
            # time.sleep(1.1) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if cts_ordno != "":
                self.parent.t0425(accno=self.datas[0], passwd=self.datas[1], expcode=self.datas[2], chegb=self.datas[3], medosu=self.datas[4], sortgb=self.datas[5], cts_ordno=cts_ordno, cont=True)

        elif tr_code == "CSPAT00600": # 현물 정상 주문.
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]
            OUT_BLOCK_2_CODE = OUT_BLOCK[2]
            OUT_BLOCK_2_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["주문1", dict(zip(OUT_BLOCK_1_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["주문1", dict(zip(OUT_BLOCK_1_NAME, item))])
            self.parent.CSPAT00600_outblock_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            item = list()
            for idx in range(len(OUT_BLOCK_2_CODE)):
                out_block_code = OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["주문2", dict(zip(OUT_BLOCK_2_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["주문2", dict(zip(OUT_BLOCK_2_NAME, item))])
            self.parent.CSPAT00600_outblock_list.append(dict(zip(OUT_BLOCK_2_NAME, item)))

        elif tr_code == "CSPAT00700": # 현물 정정 주문.
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]
            OUT_BLOCK_2_CODE = OUT_BLOCK[2]
            OUT_BLOCK_2_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["정정주문1", dict(zip(OUT_BLOCK_1_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["정정주문1", dict(zip(OUT_BLOCK_1_NAME, item))])
            self.parent.CSPAT00700_outblock_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            item = list()
            for idx in range(len(OUT_BLOCK_2_CODE)):
                out_block_code = OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["정정주문2", dict(zip(OUT_BLOCK_2_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["정정주문2", dict(zip(OUT_BLOCK_2_NAME, item))])
            self.parent.CSPAT00700_outblock_list.append(dict(zip(OUT_BLOCK_2_NAME, item)))

        elif tr_code == "CSPAT00800": # 현물 취소 주문.
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]
            OUT_BLOCK_2_CODE = OUT_BLOCK[2]
            OUT_BLOCK_2_NAME = OUT_BLOCK[3]

            item = list()
            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["취소주문1", dict(zip(OUT_BLOCK_1_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["취소주문1", dict(zip(OUT_BLOCK_1_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            self.parent.CSPAT00800_outblock_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            item = list()
            for idx in range(len(OUT_BLOCK_2_CODE)):
                out_block_code = OUT_BLOCK_2_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            self.parent.queue.put(["취소주문2", dict(zip(OUT_BLOCK_2_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(["취소주문2", dict(zip(OUT_BLOCK_2_NAME, item))]) # out_block = dict(zip(OUT_BLOCK_NAME, item))
            self.parent.CSPAT00800_outblock_list.append(dict(zip(OUT_BLOCK_2_NAME, item)))

        elif tr_code == "t1866": # 서버저장조건리스트 조회.
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            # print(out_block)

            # [수정] 연속데이터조회용 인자
            cont = out_block["연속여부"]
            cont_key = out_block["연속키"]

            # --- 한 화면내에 있는 반복 데이터 가져 오기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                self.parent.jongmok_search_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))
            
            # [수정] --- 한 화면에 다 표현 못한 데이터들 연속으로 데이터 조회
            time.sleep(3.3) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if cont == "1":
                self.parent.t1866(user_id=self.datas[0], gb=self.datas[1], group_name=self.datas[2], cont=cont, cont_key=cont_key)

        elif tr_code == "t1857": # e종목검색 조회.
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            print(f"실시간종목검색 종목 목록 : {out_block}")
            self.parent.sKey = out_block['실시간키']            
            # print("+++++ 실시간종목검색 종목 목록")
            # print(f"실시간키 : {self.parent.sKey}")
            # --- 한 화면내에 있는 반복 데이터 가져 오기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")            # print(f"총검색된 종목 수 중 현재 화면에 표시된 종목 수 : {count}")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                self.parent.searched_jongmok_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            # 왜 무한 루프에 빠진 걸까? 그래서 여기에서 response를 True로 설정하는 것으로 해결하긴 했음.
            if self.parent.searched_jongmok_list:
                self.parent.response = True

        elif tr_code == "CHARTINDEX": # Chart내 보조지표 정보 조회. 미완성
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            tr_code = "ChartIndex"
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            print("\n >>>>> OUT_BLOCK : ")
            print(out_block)

            # [수정] 연속데이터조회용 인자
            self.parent.chart_indexid = out_block["지표ID"]            # indexid = out_block["indexid"]
            rec_cnt = int(out_block["레코드갯수"])         # rec_cnt = out_block["rec_cnt"]
            validdata_cnt = int(out_block["유효데이터컬럼갯수"])         # validdata_cnt = out_block["validdata_cnt"]
            print(f"지표ID : {self.parent.chart_indexid}, 레코드갯수 : {rec_cnt}, 유효데이터컬럼갯수 : {validdata_cnt}")

            # --- 반복 데이터 조회 하기.
            # count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")  # 현재 창에 몇개의 데이터 리스트가 있는지
            count = rec_cnt
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                cnt = count - cnt - 1   # 
                # print(f"count : {count}, cnt : {cnt}")
                item = list()
                # for idx in range(len(OUT_BLOCK_1_CODE)):
                for idx in range(validdata_cnt):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
                out_block = dict(zip(OUT_BLOCK_1_NAME, item))
                # print("\n >>>>> OUT_BLOCK1 : ")
                # print(out_block)
                # [수정] 조회한 데이터 저장용 변수
                # date = item[0]     # date : 날짜. 이 값을 self.parent.chart_dict의 키 값으로 사용
                # self.parent.chart_index_dict[date]  = out_block # dict(zip(OUT_BLOCK_1_NAME, item))
                self.parent.chart_index_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            # --- 연속 데이터 조회
            # time.sleep(3.3) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            # if int(rec_cnt) == 500:
                # self.parent.ChartIndex(indexid=indexid, indexname=self.datas[1], indexparam=self.datas[2], market=self.datas[3], period=self.datas[4], shcode=self.datas[5], qrycnt=self.datas[6], ncnt=self.datas[7], sdate=self.datas[8], edate=self.datas[9], Isamend=self.datas[10], Isgab=self.datas[11], IsReal=self.datas[12], cont=True)            

        elif tr_code == "t1901": # ETF 현재가(시세) 조회.
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))
            print(out_block)
            self.parent.ETF_list.append(dict(zip(OUT_BLOCK_NAME, item)))

        elif tr_code == "t1903": # ETF 일별 추이
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))     # print(f" >>> ETF 일별추이 : OutBlock")
            # print(out_block)
            date = out_block["일자"]   

            # --- 한 화면내에 있는 반복 데이터 가져 오기.
            count = self.parent.query.GetBlockCount(f"{tr_code}OutBlock1")
            for cnt in range(count): # 일련의 데이터가 반복해서 나올 경우. 일련의 데이터를 구분해 줄 키가 필요.
                item = list()
                # cnt = count - cnt - 1   # 
                for idx in range(len(OUT_BLOCK_1_CODE)):
                    out_block_code = OUT_BLOCK_1_CODE[idx]
                    data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, cnt) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                    item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.

                # print(dict(zip(OUT_BLOCK_1_NAME, item)))  
                self.parent.ETF_daily_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))

            # [수정] --- 한 화면에 다 표현 못한 데이터들 연속으로 데이터 조회
            time.sleep(3.3) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건.           print(f"주문번호 : {cts_ordno}")
            if date != "":
                self.parent.t1903(shcode=self.datas[0], date=date, cont=True)

        elif tr_code == "t1906": # ETF LP 호가 조회
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))     # print(f" >>> ETF 일별추이 : OutBlock")

            self.parent.ETF_LP_Hoga_list.append(dict(zip(OUT_BLOCK_NAME, item)))

        elif tr_code == "t1101": # 주식 현재가 호가 조회
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_CODE = OUT_BLOCK[0]
            OUT_BLOCK_NAME = OUT_BLOCK[1]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_CODE)):
                out_block_code = OUT_BLOCK_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_NAME, item))     # print(f" >>> ETF 일별추이 : OutBlock")

            self.parent.t1101_list.append(out_block)
            self.parent.t1101_dict = out_block

        elif tr_code == "t8407": # 주식 멀티 현재가 호가 조회
            # OCCURS 속성이 없는 블럭에서 복사해서 사용할 부분. : OutBlock
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[0]
            OUT_BLOCK_1_NAME = OUT_BLOCK[1]

            # 연속 데이터 입력용 변수값 모음
            item = list()
            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldData(f"{tr_code}OutBlock1", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++                # data = self.parent.query.GetFieldData("CSPAQ12300OutBlock2", out_block_code, 0) # index:0, OCCURS일 경우는 index는 index++
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            out_block = dict(zip(OUT_BLOCK_1_NAME, item))     # print(f" >>> ETF 일별추이 : OutBlock")

            self.parent.t8407_list.append(out_block)
            self.parent.t8407_dict = out_block


    def OnReceiveSearchRealData(self, tr_code):
        # 실시간 체결
        if tr_code == "t1857": # e조건검색 실시간 데이터 받기
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldSearchRealData(f"{tr_code}OutBlock1", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            # self.searched_jongmok_list = ["e종목검색", dict(zip(OUT_BLOCK_1_NAME, item))]
            self.parent.searched_jongmok_list.append(dict(zip(OUT_BLOCK_1_NAME, item)))
            print(f"***** 실시간종목검색")
            print(self.parent.searched_jongmok_list)
            # self.parent.queue.put(["e종목검색", dict(zip(OUT_BLOCK_1_NAME, item))])

    def OnReceiveChartRealData(self, tr_code): # 미완성
        # Chart Index 실시간 데이터 받기
        if tr_code == "CHARTINDEX": # e조건검색 실시간 데이터 받기
            item = list()
            IN_BLOCK, OUT_BLOCK = menu_var_name(tr_code=tr_code)
            OUT_BLOCK_1_CODE = OUT_BLOCK[2]
            OUT_BLOCK_1_NAME = OUT_BLOCK[3]

            for idx in range(len(OUT_BLOCK_1_CODE)):
                out_block_code = OUT_BLOCK_1_CODE[idx]
                data = self.parent.query.GetFieldChartRealData(f"{tr_code}OutBlock1", out_block_code)
                item.append(data) # 하나의 필드명에 해당하는 값을 리턴받아 추가한다.
            
            print("\n >>>>> Chart Real Data : OUT_BLOCK : ")
            out_block = dict(zip(OUT_BLOCK_1_NAME, item))
            date = item[0]     # date : 날짜. 이 값을 self.parent.chart_dict의 키 값으로 사용
            # self.parent.chart_index_dict[date]  = out_block # dict(zip(OUT_BLOCK_1_NAME, item))
            self.parent.chart_index_list.append(out_block)
            print(out_block)
            # self.parent.queue.put(self.parent.chart_index_dict[date])
            self.parent.queue.put(self.parent.chart_index_list)
            # chart_index_list = ["e종목검색", dict(zip(OUT_BLOCK_1_NAME, item))]
            # print(f"실시간차트지표데이터 : {chart_index_list}")
            # self.parent.queue.put(["실시간차트지표데이터", dict(zip(OUT_BLOCK_1_NAME, item))])


class XAQuery:
    """ 
    서버로부터 데이터를 주고받는 동작을 컨트롤.
    """
    def __init__(self, login_server="모의투자", account_num=None, account_pwd=None):
        # [수정/추가] 각 함수들에서 조회한 데이터들을 저장하는 곳으로 필요할 때마다 추가해야한다.
        self.login_server = login_server
        self.account_dict = dict()
        self.account_list = list()
        self.deposit_dict = dict()
        self.chart_ntick_dict = dict()
        self.chart_min_dict = dict()
        self.chart_dict = dict()
        self.chart_list = list()
        self.chart_ntick_list = list()
        self.chart_min_list = list()
        self.t1444_list = list()
        self.t1444_dict = dict()
        self.t8424_list = list()
        self.t1441_dict = dict()
        self.t1486_list = list()
        self.t8407_list = list() # t8407
        self.t8407_dict = dict() # t8407
        self.CSPAT00600_dict = dict()
        self.CSPAT00600_outblock_list = list()
        self.CSPAT00700_dict = dict()
        self.CSPAT00700_outblock_list = list()
        self.CSPAT00800_dict = dict()
        self.CSPAT00800_outblock_list = list()
        self.CSPAQ13700_dict = dict()
        self.t0425_outblock_list = list()
        self.t0425_outblock1_list = list()
        self.jongmok_search_list = list() # t1866
        self.searched_jongmok_list = list() # t1857
        self.chart_index_dict = dict() # ChartIndex
        self.chart_index_list = list() # ChartIndex
        self.chart_indexid = ""
        self.sKey = ""  # e종목 검색 실시간키
        self.ETF_list = list() # t1901
        self.ETF_daily_list = list() # t1903
        self.ETF_LP_Hoga_list = list() # t1906
        self.t1101_list = list() # t1101
        self.t1101_dict = dict() # t1101

        # res file들이 저장된 곳.
        self.resFile_url = "C:/LS_SEC/xingAPI/Res/"

        # login() 함수에서 로그인이 성공하면 이 값을 True로 변경하여 다음 코드로 진행할 수 있도록 한다.
        self.response = False 

        # (1) XAQueryReceiver 인스턴스 생성. 즉, 자식을 만들었다.
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryReceiver)

        # XAQueryReceiver의 self.parent 변수에 접근하여 XAQuery의 self 값 즉, XAQuery 자신의 주소를 전달하여,
        # XAQueryReceiver에서 부모인 XAQuery에 접근할 수 있도록 한다.
        self.query.parent = self

        self.queue = queue.Queue()
        self.query.account_num = account_num
        self.query.password = account_pwd
        self.last_msg_is_system_error = 0
        self.last_msg_code = ""
        self.last_msg_text = ""
        self._tr_last_call_ts = {}
        self._tr_recent_call_ts = defaultdict(deque)

    def _safe_get_tr_count_base_sec(self):
        try:
            val = self.query.GetTRCountBaseSec()
            return float(val) if val is not None else 0.0
        except Exception:
            return 0.0

    def _safe_get_tr_count_limit(self, tr_code):
        try:
            val = self.query.GetTRCountLimit(tr_code)
            return int(val) if val is not None else 0
        except Exception:
            return 0

    def _safe_get_tr_count_request(self, tr_code):
        try:
            val = self.query.GetTRCountRequest(tr_code)
            return int(val) if val is not None else 0
        except Exception:
            return 0

    def _wait_for_tr_quota(self, tr_code, min_interval_sec=1.05, fallback_limit_10m=200):
        while True:
            now = time.time()
            sleep_sec = 0.0

            base_sec = self._safe_get_tr_count_base_sec()
            target_interval = max(min_interval_sec, base_sec + 0.05 if base_sec > 0 else min_interval_sec)
            last_ts = self._tr_last_call_ts.get(tr_code)
            if last_ts is not None:
                sleep_sec = max(sleep_sec, target_interval - (now - last_ts))

            dq = self._tr_recent_call_ts[tr_code]
            while dq and now - dq[0] >= 600:
                dq.popleft()

            limit_api = self._safe_get_tr_count_limit(tr_code)
            req_api = self._safe_get_tr_count_request(tr_code)
            limit = limit_api if limit_api and limit_api > 0 else fallback_limit_10m

            if limit > 0 and len(dq) >= limit:
                sleep_sec = max(sleep_sec, dq[0] + 600 - now + 0.05)

            if limit > 0 and req_api >= limit:
                # API 카운트 반영 타이밍 오차를 고려해 보수적으로 대기
                if dq:
                    sleep_sec = max(sleep_sec, dq[0] + 600 - now + 0.05)
                else:
                    sleep_sec = max(sleep_sec, 5.0)

            if sleep_sec <= 0:
                call_ts = time.time()
                self._tr_last_call_ts[tr_code] = call_ts
                dq.append(call_ts)
                return

            time.sleep(min(sleep_sec, 30.0))

    def _is_tr_rate_limited(self):
        msg_code = str(self.last_msg_code).strip()
        msg_text = str(self.last_msg_text)
        return msg_code == "-21" or ("전송제한" in msg_text)

    def _request_with_tr_rate_limit(self, tr_code, cont=False, max_retry=5):
        for attempt in range(max_retry):
            self._wait_for_tr_quota(tr_code=tr_code)
            self.last_msg_is_system_error = 0
            self.last_msg_code = ""
            self.last_msg_text = ""
            self.request(cont=cont)

            if not self._is_tr_rate_limited():
                return

            wait_sec = min(60, 5 * (2 ** attempt))
            print(f"[{tr_code}] 전송제한 감지(code={self.last_msg_code}). {wait_sec}초 대기 후 재시도합니다.")
            time.sleep(wait_sec)

        raise RuntimeError(f"TR_RATE_LIMIT:{tr_code} code={self.last_msg_code} msg={self.last_msg_text}")


    def request(self, cont=False):
        """
        # 아래 함수의 첫번째 파라미터 cont는 연속조회 여부입니다. 연속조회 일 경우에만 True이고 일반적으로는 False 입니다.
        # 지금은 최초 request 이므로, False를 입력한다.
        # 데이터양이 많아서 추가로 데이터(다음 페이지 데이터)를 연속해서 요청할 때 True를 넣어야 한다.
        # (4) 입력데이터 서버로 전송. : 이때부터, 서버에서는 별도로 요청한 데이터를 XAQueryReceiver 클래스의 2개의 함수로 비동기로 보내준다.
        #     (사실 서버에서 오는 데이터들은 큐에 들어가며 그 큐에서 데이터를 뽑아서 XAQueryReceiver 클래스로 보내주는 것은 
        #      아래 pythoncom.PumpWaitingMessages() 함수에서 수행된다.)
        #     리퀘스트가 정상적으로 접수가 되면 리턴값을 바로 보낸다. 음수(실패), 나머지(성공). 데이터는 비동기로 위 클래스로 보내준다.
        """
        res = self.query.Request(cont)
        if res < 0:
            print("데이터 요청에 실패했습니다.")
        """
        # request() 함수를 통해서 데이터 리퀘스트를 했을 경우, 최초 리퀘스트가 성공했다면 OnReceiveMessage 함수에서 self.parent.response 를 True로 설정한다.
        # 그 다음 TR을 요청할 경우에 self.parent.response 가 이미 True 상태이기 때문에, 아래 while 문이 실행이 되지 않게된다. 
        # 그래서 self.response = False를 해주어야 한다.
        """
        self.response = False    
        while not self.response:
            pythoncom.PumpWaitingMessages()

        return
    
    def request_service(self, tr_code, cont=False):
        if tr_code == "ChartIndex":
            res = self.query.RequestService(tr_code, 0)
        elif tr_code == "t1857":
            # e조건검색 (t1857), ChartIndex 용.
            res = self.query.RequestService(tr_code, "")

        if res < 0:
            print("데이터 요청에 실패했습니다.")

        """
        # request() 함수를 통해서 데이터 리퀘스트를 했을 경우, 최초 리퀘스트가 성공했다면 OnReceiveMessage 함수에서 self.parent.response 를 True로 설정한다.
        # 그 다음 TR을 요청할 경우에 self.parent.response 가 이미 True 상태이기 때문에, 아래 while 문이 실행이 되지 않게된다. 
        # 그래서 self.response = False를 해주어야 한다.
        """
        self.response = False    
        while not self.response:
            pythoncom.PumpWaitingMessages()

        return

    def request_balance(self, account_num, password, cont=False): # 현물계좌 잔고내역 조회
        """ 현물계좌 잔고내역 조회 : CSPAQ12300 """
        tr_code = "CSPAQ12300"

        if cont == False:
            self.account_list = list()

        datas = [1, account_num, password, "0", "1", "0", "1"]  # InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        #-------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1", block_codes[idx], 0, datas[idx])

        # for idx in range(len(datas)):
        #     self.query.SetFieldData(f"{tr_code}InBlock1", CSPAQ12300_IN_BLOCK_CODE[idx], 0, datas[idx])

        time.sleep(1.1)
        self.request(cont=cont)

        return self.account_dict, self.account_list

    def request_deposit(self, account_num, password): # 현물계좌 예수금/주문가능금액/총평가 조회
        """ 
        현물계좌 예수금/주문가능금액/총평가 조회 : CSPAQ22200, HTS 화면번호(6202) 
        """
        tr_code = "CSPAQ22200"  # 수정.
        datas = [1, "", account_num, password, "0"] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1",  CSPAQ22200_IN_BLOCK_CODE[idx], 0, datas[idx])

        time.sleep(1.1)
        self.request()
        return self.deposit_dict

    # def CSPAQ13700(self, account_num, password): # 현물계좌 주문체결내역 조회
    def CSPAQ13700(self, account_num=None, password=None, OrdMktCode="00", BnsTpCode="0", IsuNo="", ExecYn="0", OrdDt="", SrtOrdNo2="0", BkseqTpCode="1", OrdPtnCode="00"):  # 현물계좌 주문체결내역 조회      
        """ 
        현물계좌 주문체결내역 조회 : CSPAQ13700 
        account_num : 계좌번호, 
        password : 입력비밀번호, 
        OrdMktCode : 주문시장 코드. "00:전체, 10:거래소, 20:코스닥, 30:프리보드", 
        BnsTpCode : 매매구분. "0: 전체, 1:매도, 2:매수", 
        IsuNo : 종목번호. "", 
        ExecYn : 체결여부. "0:전체, 1:체결, 3:미체결", 
        OrdDt : 주문일. "", 
        SrtOrdNo2 : 시작주문번호2. "", 
        BkseqTpCode : 역순구분. "0:역순, 1:정순", 
        OrdPtnCode : 주문유형코드. "00:전체, 98:매도전체, 99:매수전체, 01:현금매도, 02:현금매수". 다른 코드들도 있으니 필요시 참조할 것.
        """
        if IsuNo != "":
            IsuNo = f"A{IsuNo}"

        tr_code = "CSPAQ13700"
        datas = [1, account_num, password, OrdMktCode, BnsTpCode, IsuNo, ExecYn, OrdDt, SrtOrdNo2, BkseqTpCode, OrdPtnCode] # InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1", CSPAQ13700_IN_BLOCK_CODE[idx], 0, datas[idx])

        self.request()
        return self.account_dict

    def t8410(self, shcode="", gubun="일", qrycnt=500, sdate="", edate="당일", cts_date="", comp_yn="N", sujung="Y", cont=False): # 주식차트(일주월년년)
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        shcode : 단축 종목 코드
        gubun : 주기구분(2:일, 3:주, 4:월, 5:년)
        qrycnt : 요청건수(최대-압축:2000비압축:500)
        sdate : 시작일자
        edate : 종료일자
        cts_date :연속일자
        comp_yn : 압축여부(Y:압축N:비압축)
        sujung : 수정주가여부(Y:적용, N:비적용)
        """
        tr_code = "t8410"   # 수정

        if cont == False:
            self.chart_list = list()

        gubun = {"일":"2", "주":"3", "월":"4", "년":"5"}.get(gubun, gubun) # "주기구분 값 입력 바랍니다.")
        # (3-0) 입력데이터 설정.
        datas = [shcode, gubun, qrycnt, sdate, edate, cts_date, comp_yn, sujung] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas
        self.chart_dict = dict()
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])   # self.query.SetFieldData(f"{tr_code}InBlock",  T8410_IN_BLOCK_CODE[idx], 0, datas[idx]) # 수정

        # (4) 입력데이터 서버로 전송.
        self._request_with_tr_rate_limit(tr_code=tr_code, cont=cont, max_retry=5)

        # return self.chart_dict
        return self.chart_list

    def t1486(self, shcode="", cts_time="085959", cnt='', exchgubun="K", cont=False): # 주식차트(일주월년년)
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        shcode : 단축 종목 코드
        cts_time :시간CTS
        cnt : 조회건수
        exchgubun : 거래소구분코드
        """
        tr_code = "t1486"   # 수정

        if cont == False:
            self.t1486_list = list()

        exchgubun = {"KRX":"K", "NXT":"N", "통합":"U", "K":"K"}.get(exchgubun, exchgubun) # "주기구분 값 입력 바랍니다.")
        # (3-0) 입력데이터 설정.
        datas = [shcode, cts_time, cnt, exchgubun] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas

        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        time.sleep(1.2)

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        # return self.chart_dict
        return self.t1486_list

    def t8411(self, shcode="005930", ncnt="1", qrycnt=500, nday="0", sdate="", edate="당일", cts_date="", cts_time="", comp_yn="N", cont=False): # 주식차트(틱/n틱)
        """
        shcode : 단축 종목 코드
        ncnt : 단위 (n 틱)
        qrycnt : 요청건수(최대-압축:2000비압축:500)
        sdate : 시작일자
        edate : 종료일자
        cts_date :연속일자
        cts_time : 연속시간
        comp_yn : 압축여부(Y:압축N:비압축)
        """
        tr_code = "t8411"   # 수정
        if cont == False:
            self.chart_ntick_list = list()

        # (3-0) 입력데이터 설정.
        datas = [shcode, ncnt, qrycnt, nday, sdate, edate, cts_date, cts_time, comp_yn] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  T8411_IN_BLOCK_CODE[idx], 0, datas[idx]) # 수정

        time.sleep(1)
        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        return self.chart_ntick_list

    def t8412(self, shcode="005930", ncnt="1", qrycnt=500, nday="0", sdate="", stime="", edate="당일", etime="", cts_date="", cts_time="", comp_yn="N", cont=False): # 주식차트(N분)
        """
        shcode : 단축 종목 코드
        ncnt : 단위 (n 분). 0:30초, 1:1분, ...
        qrycnt : 요청건수(최대-압축:2000비압축:500). 500
        sdate : 시작일자
        stime : 사용안함
        edate : 종료일자
        etime : 사용안함
        cts_date :연속일자
        cts_time : 연속시간
        comp_yn : 압축여부(Y:압축N:비압축)
        cont : 연속조회여부
        """
        tr_code = "t8412"   # 수정
        if cont == False:
            self.chart_min_list = list()

        # (3-0) 입력데이터 설정.
        datas = [shcode, ncnt, qrycnt, nday, sdate, stime, edate, etime, cts_date, cts_time, comp_yn] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas
        # self.chart_min_dict = dict()
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])   # self.query.SetFieldData(f"{tr_code}InBlock",  T8412_IN_BLOCK_CODE[idx], 0, datas[idx]) # 수정

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        return self.chart_min_list

    def t8430(self, gubun="1", cont=False):
        """
        주식 종목 조회
        gubun : 구분(0:전체, 1:코스피, 2:코스닥)
        cont : 연속조회여부
        """
        tr_code = "t8430"
        # (3-0) 입력데이터 설정.
        datas = [gubun] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  T8430_IN_BLOCK_CODE[idx], 0, datas[idx]) # 수정

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

    def t8451(self, shcode="005930", gubun="일", qrycnt=500, sdate="", edate="당일", cts_date="", comp_yn="N", sujung="Y", exchgubun='K', cont=False): # (통합)주식차트(일주월년년)
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        shcode : 단축 종목 코드
        gubun : 주기구분(2:일, 3:주, 4:월, 5:년)
        qrycnt : 요청건수(최대-압축:2000비압축:500)
        sdate : 시작일자
        edate : 종료일자
        cts_date :연속일자
        comp_yn : 압축여부(Y:압축N:비압축)
        sujung : 수정주가여부(Y:적용, N:비적용)
        exchgubun : 거래소구분(K: KRX, N:NXT, U:통합) 그외 입력값은 KRX로 대체한다.
        """
        tr_code = "t8451"   # 수정

        if cont == False:
            self.chart_list = list()

        gubun = {"일":"2", "주":"3", "월":"4", "년":"5"}.get(gubun, gubun) # "주기구분 값 입력 바랍니다.")
        # (3-0) 입력데이터 설정.
        datas = [shcode, gubun, qrycnt, sdate, edate, cts_date, comp_yn, sujung, exchgubun] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas
        self.chart_dict = dict()
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])   # self.query.SetFieldData(f"{tr_code}InBlock",  T8451_IN_BLOCK_CODE[idx], 0, datas[idx]) # 수정
        time.sleep(1)
        # time.sleep(3.3) # 한 번에 많은 조회를 하는 것을 조심해야 함. 10분당 200건. 

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        # return self.chart_dict
        return self.chart_list

    def t1444(self, upcode="", idx="", cont=False): # 시가총액상위
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        시가총액 상위 조회 : t1444
        upcode : 업종코드.
        idx : 연속출력용 IDX
        cont : 다음 데이터 출력
        """
        # [수정]
        tr_code = "t1444"  
        if cont == False:
            self.t1444_list = list()
        return_dict = self.t1444_list
        
        # (3-0) 입력데이터 설정.
        datas = [upcode, idx] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        return return_dict  
    
    def t8424(self, gubun1="0", cont=False): # 업종 코드
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        전체 업종 조회 : t8424
        upcode : 업종코드.
        idx : 연속출력용 IDX
        cont : 다음 데이터 출력
        """
        # [수정]
        tr_code = "t8424"  
        if cont == False:
            self.t8424_list = list()

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t8424).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]
        # datas = list(dict(locals()).values())[1:-1]  # self, cont 제외한 값만 리스트에 저장        
        # datas = [gubun1] # 수정. InBlock1에 넣을 데이터들. 필드 순서에 맞게 넣는다.
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        print(datas)
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        return self.t8424_list     
    
    def t1441(self, gubun1="2", gubun2="0", gubun3="0", jc_num=0x85004380, sprice="", eprice="", volume="", idx="", jc_num2=0x000000ff, cont=False): # 등락율 상위
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        전체 업종 조회 : t8424
        upcode : 업종코드.
        idx : 연속출력용 IDX

        jc_num : 대상제외값. 중복 제외하려면 값들을 모두 더하면 된다. 예: 0x85004380
            증거금50 : 0x00400000,  증거금100 : 0x00800000,     증거금50/100 : 0x00200000,  관리종목 : 0x00000080, 시장경보 : 0x00000100, 거래정지 : 0x00000200
            우선주 : 0x00004000,    투자유의 : 0x04000000,      정리매매 : 0x01000000,      불성실공시 : 0x80000000, 
        jc_num2 : 대상제외값. 중복 제외하려면 값들을 모두 더하면 된다. 예: (0x000000ff)
            기본 : 000000000000, 상장지수펀드 : 000000000001, 선박투자회사 : 000000000002, 스펙 : 000000000004, ETN : 000000000008(0x00000008)
            투자주의 : 000000000016(0x00000010), 투자위험 : 000000000032(0x00000020), 위험예고 : 000000000064(0x00000040), 담보불가 : 000000000128(0x00000080)
        cont : 다음 데이터 출력
        """
        # [수정]
        tr_code = "t1441"  
        if cont == False:
            self.t1441_list = list()
        return_dict = self.t1441_list        # return_dict = self.t1441_dict
        
        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1441).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        print(datas)
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        time.sleep(1.1)
        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)

        return return_dict      

    def CSPAT00600(self, AcntNo, InptPwd, IsuNo="", OrdQty=1, OrdPrc="", BnsTpCode="", OrdprcPtnCode="지정가", MgntrnCode="000", LoanDt="", OrdCndiTpCode="0", MbrNo="KRX"): # 현물 매수/매도 주문.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        현물 매수/매도 주문 : CSPAT00600
        AcntNo : 계좌번호
        InptPwd : 계좌비밀번호
        IsuNo : 종목번호. [주식/ETF : 종목코드 or A+종목코드(모의투자는 A+종목코드)]
        OrdQty : 주문수량
        OrdPrc : 주문가격
        BnsTpCode : 매매구분 [매수, 매도]
        OrdprcPtnCode : 호가유형코드. [지정가": "00", "시장가": "03", "조건부지정가": "05", "최유리지정가": "06", "최우선지정가": "07", "장개시전시간외종가": "61", "시간외종가": "81", "시간외단일가": "82"]
        MgntrnCode : 신용거래코드. ["000" : 보통]
        LoanDt : 대출일
        OrdCndiTpCode : 주문조건구분. {"": "0", "IOC": "1", "FOK": "2"}
        MbrNo : 회원사번호. {"KRX", "NXT"}
        """
        # [수정]
        tr_code = "CSPAT00600"  
        return_dict = self.CSPAT00600_dict
        self.CSPAT00600_outblock_list = list()

        #-----------------------------------------------------------------------------------------------------
        if BnsTpCode == "매수":
            BnsTpCode = "2"
        elif BnsTpCode == "매도":
            BnsTpCode = "1"
        else:
            print(f"[매수/매도주문] {tr_code} | {BnsTpCode} : 매매구분(매수/매도)을 명확히 입력해 주세요.")
            sys.exit()

        if self.login_server == "모의투자":
            # IsuNo = f"A{IsuNo}"
            if not IsuNo.startswith('A'):
                IsuNo = 'A' + IsuNo

        HogaType = {"지정가": "00", "시장가": "03", "조건부지정가": "05", "최유리지정가": "06", "최우선지정가": "07", "장개시전시간외종가": "61", "시간외종가": "81", "시간외단일가": "82"}
        if OrdprcPtnCode in HogaType.keys():
            OrdprcPtnCode = HogaType[OrdprcPtnCode]
        else:
            print(f"[매수/매도주문] 호가유형코드[{OrdprcPtnCode}]를 확인하세요.")
            sys.exit()

        OrderConditionCode = {"0": "0", "IOC": "1", "FOK": "2"}
        if OrdCndiTpCode in OrderConditionCode.keys():
            OrdCndiTpCode = OrderConditionCode[OrdCndiTpCode]
        else:
            print(f"[매수/매도주문] 주문조건코드 [{OrdCndiTpCode}]를 확인하세요.")
            sys.exit()
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.CSPAT00600).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # print(f"현물 매수/매도 주문 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_1_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1",  block_codes[idx], 0, datas[idx])

        time.sleep(1.1)
        # (4) 입력데이터 서버로 전송.
        self.request(False)
        # res = self.query.Request(False)
        # if res < 0:
        #     print("데이터 요청에 실패했습니다.")
        
        return self.CSPAT00600_outblock_list

    def CSPAT00800(self, OrgOrdNo, AcntNo, InptPwd, IsuNo, OrdQty): # 현물 취소 주문.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        현물 매수/매도 주문 : CSPAT00800
        OrgOrdNo : 원주문번호
        AcntNo : 계좌번호
        InptPwd : 계좌비밀번호
        IsuNo : 종목번호. [주식/ETF : 종목코드 or A+종목코드(모의투자는 A+종목코드)]
        OrdQty : 주문수량
        """
        # [수정]
        tr_code = "CSPAT00800"  
        return_dict = self.CSPAT00800_dict
        self.CSPAT00800_outblock_list = list()
        
        #-----------------------------------------------------------------------------------------------------
        if OrgOrdNo == "":
            print(f"[취소주문] 원주문번호[{OrgOrdNo}]를 확인하세요!")
            sys.exit()

        if self.login_server == "모의투자":
            # IsuNo = f"A{IsuNo}"
            if not IsuNo.startswith('A'):
                IsuNo = 'A' + IsuNo            
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.CSPAT00800).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # print(f"현물 취소 주문 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_1_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1",  block_codes[idx], 0, datas[idx])

        # self.query.SetFieldData(f"{tr_code}InBlock1",  OrgOrdNo, 0, OrgOrdNo)
        # self.query.SetFieldData(f"{tr_code}InBlock1",  AcntNo, 0, AcntNo)
        # self.query.SetFieldData(f"{tr_code}InBlock1",  InptPwd, 0, InptPwd)
        # self.query.SetFieldData(f"{tr_code}InBlock1",  IsuNo, 0, IsuNo)        
        # self.query.SetFieldData(f"{tr_code}InBlock1",  OrdQty, 0, OrdQty)

        time.sleep(0.5)
        # (4) 입력데이터 서버로 전송.
        self.request(False)
        # res = self.query.Request(False)
        # if res < 0:
        #     print("데이터 요청에 실패했습니다.")
        
        # return return_dict      
        return self.CSPAT00800_outblock_list
    
    def CSPAT00700(self, OrgOrdNo, AcntNo, InptPwd, IsuNo, OrdQty, OrdprcPtnCode, OrdCndiTpCode="0", OrdPrc=10000000): # 현물 정정 주문.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        현물 정정 주문 : CSPAT00700
        OrgOrdNo : 원주문번호
        AcntNo : 계좌번호
        InptPwd : 계좌비밀번호
        IsuNo : 종목번호. [주식/ETF : 종목코드 or A+종목코드(모의투자는 A+종목코드)]
        OrdQty : 주문수량
        OrdprcPtnCode : 호가유형코드 
        OrdCndiTpCode : 주문조건 구분
        OrdPrc : 주문가 
        """
        # [수정]
        tr_code = "CSPAT00700"  
        return_dict = self.CSPAT00700_dict
        self.CSPAT00700_outblock_list = list()

        #-----------------------------------------------------------------------------------------------------
        if OrgOrdNo == "":
            print(f"[정정주문] : 원주문번호[{OrgOrdNo}]를 확인하세요!")
            sys.exit()

        if self.login_server == "모의투자":
            # IsuNo = f"A{IsuNo}"
            if not IsuNo.startswith('A'):
                IsuNo = 'A' + IsuNo

        HogaType = {"지정가": "00", "시장가": "03", "조건부지정가": "05", "최유리지정가": "06", "최우선지정가": "07", "장개시전시간외종가": "61", "시간외종가": "81", "시간외단일가": "82"}
        if OrdprcPtnCode in HogaType.keys():
            OrdprcPtnCode = HogaType[OrdprcPtnCode]
        else:
            print(f"[정정주문] 호가유형코드[{OrdprcPtnCode}]를 확인하세요.")
            sys.exit()

        OrderConditionCode = {"0": "0", "IOC": "1", "FOK": "2"}
        if OrdCndiTpCode in OrderConditionCode.keys():
            OrdCndiTpCode = OrderConditionCode[OrdCndiTpCode]
        else:
            print(f"[정정주문] 주문조건코드 [{OrdCndiTpCode}]를 확인하세요.")
            sys.exit()

        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.CSPAT00700).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # print(f"현물 취소 주문 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_1_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock1",  block_codes[idx], 0, datas[idx])

        # (4) 입력데이터 서버로 전송.
        self.request(False)
        
        # return return_dict       
        return self.CSPAT00700_outblock_list

    def t0425(self, accno, passwd, expcode, chegb, medosu, sortgb="주문번호순", cts_ordno="", cont=False): # 주식 체결/미체결.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        주식 체결/미체결결 : t0425
        accno : 계좌번호
        passwd : 계좌비밀번호
        expcode : 종목번호.
        chegb : 체결구분. {"전체": "0", "체결": "1", "미체결": "2"}
        medosu : 매매구분. {"전체": "0", "매도": "1", "매수": "2"}
        sortgb : 정렬순서. {"주문번호순": "2", "주문번호역순": "1"}
        cts_ordno : 연속주문번호.
        cont : 연속조회(True)
        """
        # [수정]
        tr_code = "t0425"  
        if cont == False:
            self.t0425_outblock_list = list() # 주식 현재가 호가 조회
            self.t0425_outblock1_list = list() # 주식 현재가 호가 조회
        # return_dict = self.t0425_list
        
        #-----------------------------------------------------------------------------------------------------
        chegb_dict = {"전체": "0", "체결": "1", "미체결": "2"}
        
        chegb = str(chegb)
        medosu = str(medosu)
        sortgb = str(sortgb)

        if chegb in chegb_dict.keys(): 
            chegb = chegb_dict[chegb]
        else: 
            if chegb not in ["0", "1", "2"]:
                print(f"체결구분(chegb)을 [{chegb}] 에서 전체['0']으로 강제 설정했습니다.")
                chegb = "0" # 전체로 강제 설정

        medosu_dict = {"전체": "0", "매도": "1", "매수": "2"}
        if medosu in medosu_dict.keys(): 
            medosu = medosu_dict[medosu]
        else: 
            if medosu not in ["0", "1", "2"]:
                print(f"매매구분(medosu)을 [{medosu}]에서 전체['0']으로 강제 설정했습니다.")
                medosu = "0" # 전체로 강제 설정

        sortgb_dict = {"주문번호순": "2", "주문번호역순": "1"}
        if sortgb in sortgb_dict.keys(): 
            sortgb = sortgb_dict[sortgb]
        else: 
            if sortgb not in ["2", "1"]:
                print(f"정렬방법(sortgb)을 [{sortgb}]에서 주문번호역순['1']으로 강제 설정했습니다.")
                sortgb = "1" # 주문번호역순으로 강제 설정
            # return
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t0425).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        # (4) 입력데이터 서버로 전송.
        time.sleep(1.1)
        self.request(cont=cont)
        
        return self.t0425_outblock_list, self.t0425_outblock1_list

    def t1901(self, shcode=""): # ETF 현재가(시세) 조회.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        ETF 현재가(시세) 조회 : t1901
        shcode : 단축코드
        """
        # [수정]
        tr_code = "t1901"  
        return_dict = self.searched_jongmok_list
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1901).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        print(f"ETF 현재가(시세) 조회 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        # time.sleep(3.3)

        # (4) 입력데이터 서버로 전송.
        self.request(False)
        
        return return_dict        

    def t1903(self, shcode="", date="", cont=False): # ETF 일별추이이.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        ETF 일별추이 : t1903
        shcode : 단축코드
        date : 연속조회키. 연속 조회시 이 값을 InBlock의 date 필드에 넣어준다.
        """
        # [수정]
        tr_code = "t1903"  
        return_dict = self.ETF_daily_list # 일별추이 저장용.
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1901).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # print(f"ETF 현재가(시세) 조회 인수들 : {datas}")
        # #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        # var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        # block_codes = globals()[var_name]
        # for idx in range(len(datas)):
        #     self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])
        #     print(f" >>> (5) ETF 일별추이 입력 변수들 : {block_codes[idx]} : {datas[idx]}")

        self.query.SetFieldData(f"{tr_code}InBlock",  "shcode", 0, shcode)
        self.query.SetFieldData(f"{tr_code}InBlock",  "date", 0, date)

        # (4) 입력데이터 서버로 전송.
        self.request(cont=cont)
        
        return return_dict      

    def t1906(self, shcode=""): # ETF LP 호가.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        ETF LP 호가 : t1906
        shcode : 단축코드
        """
        # [수정]
        tr_code = "t1906"  
        return_dict = self.ETF_LP_Hoga_list # LP 호가 저장용.
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1901).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        self.query.SetFieldData(f"{tr_code}InBlock",  "shcode", 0, shcode)

        # (4) 입력데이터 서버로 전송. 1번만 호출함.
        self.request(False)
        
        return return_dict   

    def t1101(self, shcode=""): # 주식 현재가 호가 조회
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        주식 현재가 호가 조회 : t1101
        shcode : 단축코드
        """
        # [수정]
        tr_code = "t1101"  
        self.t1101_list = list() # 주식 현재가 호가 조회
        return_dict = self.t1101_list # 주식 현재가 호가 조회
        # return_dict = self.t1101_dict # 주식 현재가 호가 조회
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1101).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        self.query.SetFieldData(f"{tr_code}InBlock",  "shcode", 0, shcode)

        time.sleep(0.5)
        # (4) 입력데이터 서버로 전송. 1번만 호출함.
        self.request(False)
        
        return return_dict   

    def t8407(self, nrec=1, shcode="", cont=False): # 주식 멀티 현재가 호가 조회
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        주식 현재가 호가 조회 : t1101
        shcode : 단축코드
        """
        # [수정]
        tr_code = "t8407"
        self.t8407_list = list() # 주식 멀티 현재가 호가 조회
        return_dict = self.t8407_list # 주식 멀티 현재가 호가 조회
        # return_dict = self.t8407_dict # 주식 멀티 현재가 호가 조회
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1101).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        self.query.SetFieldData(f"{tr_code}InBlock",  "nrec", 0, nrec)
        self.query.SetFieldData(f"{tr_code}InBlock",  "shcode", 0, shcode)

        time.sleep(1.1)
        # (4) 입력데이터 서버로 전송. 1번만 호출함.
        self.request(cont=cont)
        
        return return_dict  

    def t1866(self, user_id="", gb="0", group_name="", cont="0", cont_key=""): # 서버저장조건리스트 조회.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        서버저장조건리스트 조회 : t1866
        user_id : 로그인 ID
        gb : 조회구분. 0 : 그룹+조건리스트 조회, 1 : 그룹리스트조회, 2 : 그룹명에 속한 조건리스트조회
        group_name : 그룹명. 조회구분 2일 경우만 입력
        cont : 연속여부 0, 1(다음데이타 있음)
        cont_key : 연속키
        조회 제한 : 1초당 1건, 10분당 200건
        """
        # [수정]
        tr_code = "t1866"  
        if cont == "":
            self.jongmok_search_list = list()
        return_dict = self.jongmok_search_list
        
        #-----------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1866).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self"]]

        # print(f"현물 매수/매도 주문 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        # (4) 입력데이터 서버로 전송.
        # self.query.Request(False)
        if cont == "0" or cont=="":
            self.request(False)
        else:
            self.request(True)
        
        return return_dict           

    def t1857(self, sRealFlag="", sSearchFlag="0", query_index=""): # e종목 검색.
        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        e종목 검색 : t1857
        sRealFlag : 실시간구분 (0: 조회, 1:실시간)
        sSearchFlag : 종목검색구분(F: 파일, S: 서버)
        query_index : 종목검색입력값
        조회 제한 : 1초당 1건, 10분당 200건

        1. 조건검색으로 3000 종목이 검색되어도 연속조회는 없다. 한 번에 다 나온다.
        2. 조건검색 종목이 200건을 초과하면 실시간은 무시되고 단일 조회만 된다.
        3. 조건검색을 실시간용으로 등록할 수 있는 조건검색식의 갯수는 2개이다.
        2020년 12월 10일 기준.
        """
        # [수정]
        tr_code = "t1857"  
        self.searched_jongmok_list = list() # 이전에 조회한 데이터 삭제.
        return_dict = self.searched_jongmok_list
        
        #-----------------------------------------------------------------------------------------------------
        if sRealFlag == "실시간":
            sRealFlag = "1"
        elif sRealFlag == "조회":
            sRealFlag = "0"
        else:
            print("실시간 또는 조회 를 입력하세요")
            return
        if sSearchFlag == "파일":
            sSearchFlag = "F"
        elif sSearchFlag == "서버":
            sSearchFlag = "S"
        else:
            print("파일 또는 서버 를 입력하세요")
            return
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.t1857).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self"]]        # print(f"e종목 검색 인수들 : {datas}")

        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        time.sleep(1.1)

        # 실시간 해제
        if self.sKey != "":
            self.query.RemoveService(tr_code, self.sKey)
        # (4) 입력데이터 서버로 전송.
        self.request_service(tr_code, False)
         
        return return_dict    
    
    def ChartIndex(self, indexid="", indexname="", indexparam="", market="주식", period="일", shcode="", qrycnt=500, ncnt="", sdate="", edate="", Isamend="1", Isgab="1", IsReal="0", cont=False):        #------- 수정 필요 -------------------------------------------------------------------------------------------------------------------
        """
        Chart 지표 데이터 조회 : ChartIndex
        차트 지표데이터 조회 (HTS '[4201]xing차트1'의 수식관리자 내 지표 기능 제공)
        indexid : 지표ID
        indexname : 지표명. [DevCenter-수식관리자]의 지표명 (동일한 지표명을 넣어야 함 - 띄어쓰기등에 유의)
        indexparam : 지표조건설정. [DevCenter-수식관리자] 화면의 지표조건설정 : 공백이면 기본조건, 입력값이 여러개인 경우 ',' 로 연결
        market : 시장구분. 주식:1 업종:2 선물옵션:5
        period : 주기구분. 틱:0 분:1 일:2 주:3 월:4
        shcode : 단축코드
        qrycnt : 요청건수(최대 500개)
        ncnt : 단위(n틱/n분). 틱/분 조회시 해당
        sdate : 시작일자
        edate : 종료일자
        Isamend : 수정주가 반영 여부. 0:보정안함 1:보정
        Isgab : 갭보정 여부. 0:보정안함 1:보정
        IsReal : 실시간 데이터수신 자동등록 여부 (1 : API 내부에서 자동 등록)
        조회 제한 : 1초당 1건, 10분당 200건
        """
        # [수정]
        tr_code = "ChartIndex"  

        self.chart_index_list = list()

        return_dict = self.chart_index_list
        
        #-----------------------------------------------------------------------------------------------------
        # _market = {"주식":"1", "업종":"2", "선물옵션":"5"}
        # market = _market[market]
        market = {"주식":"1", "업종":"2", "선물옵션":"5"}.get(market, market) # "시장구분 값 입력 바랍니다.")
        period = {"틱":"0", "분":"1", "일":"2", "주":"3", "월":"4"}.get(period, period)  # "차트 주기 정보 입력 바랍니다.")
        #-----------------------------------------------------------------------------------------------------

        # (3-0) 입력데이터 설정.
        # 현재 함수의 로컬 변수를 먼저 저장
        local_vars = dict(locals())  # locals()의 현재 상태 저장
        # 현재 함수의 인수 목록 가져오기
        arg_names = inspect.signature(self.ChartIndex).parameters.keys()
        # self와 cont를 제외하고 리스트 생성
        datas = [local_vars[arg] for arg in arg_names if arg not in ["self", "cont"]]

        # print(f"현물 매수/매도 주문 인수들 : {datas}")
        #------- 수정 불필요 -------------------------------------------------------------------------------------------------------------------
        self.query.datas = datas # 반복조회용 입력값 저장
        # (2) RES 등록.
        self.query.ResFileName = f"{self.resFile_url}{tr_code}.res"
        # (3) 이전 indexid 값이 있다면, 차트지표데이터를 해제.
        print(f">>>>> 1 symbol : {shcode}, self.chart_indexid : {self.chart_indexid}")
        if self.chart_indexid != "":
            print(f">>>>> 2 symbol : {shcode}, self.chart_indexid : {self.chart_indexid}")
            self.query.RemoveService("ChartIndex", self.chart_indexid)
        # (3-1) 입력데이터 설정.
        var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
        block_codes = globals()[var_name]
        for idx in range(len(datas)):
            self.query.SetFieldData(f"{tr_code}InBlock",  block_codes[idx], 0, datas[idx])

        time.sleep(1.1)

        # (4) 입력데이터 서버로 전송.
        self.request_service(tr_code, False)
        
        return return_dict    
