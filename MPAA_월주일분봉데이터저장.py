# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(r"D:\_MPAA_Project\MPAA_Gemini\src\utils")
sys.path.append(r"D:\_MPAA_Project\MPAA_Gemini\src\config")
sys.path.append(r"D:\_MPAA_Project\MPAA_Gemini\src\core")
import logging

# -*- coding: utf-8 -*-
import sqlite3
import time
from datetime import datetime, timedelta
import pandas as pd
import pythoncom
from collections import deque

# 필요한 모듈 임포트 (첨부 문서 기반)
from src.config.crypto_wallet import CRYPTO_WALLET
from src.core.xa_session import XASession
from src.core.xa_query import XAQuery
from src.config.invest_items import MPAA  # invest_items.py에서 MPAA 불러옴

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class Main:

    def __init__(self, period, period_value):

        # DB 경로 설정
        DB_PRICE_DAILY = r"D:\_MPAA_Project\MPAA_Gemini\MPAA_price.db"  # 종목별 시세 DB 경로
        DB_PRICE_MIN = r"D:\_MPAA_Project\MPAA_Gemini\MPAA_price_min.db"  # 분봉 시세 DB 경로

        login_server = "모의투자" # "실투자"

        self.save_MonthWeeklyDaily_values(_src_db_path=DB_PRICE_DAILY, _dest_db_path=DB_PRICE_MIN, _period="minute", _period_value=10, _login_server=login_server, _sessioni_disconnect=False)
        logging.info("분봉 데이터 저장 완료.")
        self.save_MonthWeeklyDaily_values(_src_db_path=DB_PRICE_DAILY, _dest_db_path=DB_PRICE_MIN, _period="daily", _period_value=10, _login_server=login_server, _sessioni_disconnect=False)
        self.save_MonthWeeklyDaily_values(_src_db_path=DB_PRICE_DAILY, _dest_db_path=DB_PRICE_MIN, _period="weekly", _period_value=10, _login_server=login_server, _sessioni_disconnect=False)
        self.save_MonthWeeklyDaily_values(_src_db_path=DB_PRICE_DAILY, _dest_db_path=DB_PRICE_MIN, _period="monthly", _period_value=10, _login_server=login_server, _sessioni_disconnect=True)
        logging.info("일봉 데이터 저장 완료.")
       

    def save_min_values(self, _src_db_path=None, _dest_db_path=None, _period="minute", _period_value=10, _login_server=None, _sessioni_disconnect=True):
        """
        함수 설명:
        0. MPAA_price.db의 asset_info 테이블 구조를 복사해 MPAA_price_min.db 생성 (파일 없을 경우).
        - period_value 필드 추가.
        1. invest_items.py (MPAA)의 모든 종목에 대해 10분봉 데이터 (open, close) 조회.
        2. 9시부터 11시까지의 데이터만 필터링.
        3. xingAPI 서버 접속부터 데이터 저장까지 수행.
        4. DB: MPAA_price_min.db의 asset_info 테이블에 저장.
        - date: YYYY-MM-DD HH:MM:SS (봉 시간 포함)
        - asset_type: MPAA의 key (e.g., '국가', '섹터' 등)
        - code: 종목코드
        - period: 'minute'
        - period_value: 10
        - value_type: 'open' 또는 'close'
        - value: 해당 값
        5. 개선: 어제까지 저장된 데이터 확인 후, 오늘(15:30 이후) 또는 어제(15:30 전) 데이터만 추가 조회.
        6. 추가 개선: DB에 저장되지 않은 데이터만 조회하여 추가 (전체 데이터 조회 최소화).
        7. t8412 제한 반영: 1초당 1건, 10분당 200건 제한 준수.
        """
        
        logging.info("분봉 데이터 저장 시작...")

        # 현재 시간 확인 (2025-09-05 05:32 PM KST)
        now = datetime.now()
        cutoff_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
        target_date = now.date() if now >= cutoff_time else (now - timedelta(days=1)).date()
        target_date_str = target_date.strftime("%Y%m%d")
        
        # DB 경로 설정
        src_db_path = _src_db_path if _src_db_path else self.DB_PRICE_DAILY
        dest_db_path = _dest_db_path if _dest_db_path else self.DB_PRICE_MIN

        
        # 0. DB 생성 및 구조 복사 (파일 없을 경우)
        if not os.path.exists(dest_db_path):
            conn_src = sqlite3.connect(src_db_path)
            conn_dest = sqlite3.connect(dest_db_path)
            
            schema_query = "SELECT sql FROM sqlite_master WHERE type='table' AND name='asset_info'"
            schema = conn_src.execute(schema_query).fetchone()
            
            if schema:
                create_sql = schema[0]
                conn_dest.execute(create_sql)
                conn_dest.execute("ALTER TABLE asset_info ADD COLUMN period_value INTEGER")
                conn_dest.commit()
                print("[DB 생성] MPAA_donna_min.db 생성 및 asset_info 테이블 구조 복사 완료. period_value 필드 추가.")
            else:
                print("[오류] 원본 DB에 asset_info 테이블이 없습니다.")
                return
            
            conn_src.close()
            conn_dest.close()
        
        # MPAA에서 모든 종목 코드와 asset_type 매핑 추출
        code_to_asset_type = {}
        for asset_type, items in MPAA.items():
            for code in items.keys():
                code_to_asset_type[code] = asset_type
        
        all_codes = list(code_to_asset_type.keys())
        print(f"[종목 목록] 총 {len(all_codes)}개 종목 조회 시작.")
        
        # 1. xingAPI 서버 접속 및 로그인
        login_server = _login_server
        crypto_wallet = CRYPTO_WALLET[login_server]
        account_pwd = crypto_wallet["acc_pwd"]

        session = XASession(login_server)
        session.connect_server()
        session.login(crypto_wallet)
        
        if not session.response:
            print("[오류] 로그인 실패.")
            session.disconnect_server()
            return
        
        print("[로그인] 서버 접속 및 로그인 성공.")
        
        period = _period # "minute"
        period_value = _period_value # 10
        
        # XAQuery 인스턴스 생성
        query = XAQuery()
        
        # 기존 데이터 확인 (저장된 날짜와 코드별 마지막 시간)
        conn_dest = sqlite3.connect(dest_db_path)
        cur = conn_dest.cursor()
        cur.execute("""
            SELECT date, code FROM asset_info 
            WHERE period='minute' AND period_value=10 
            ORDER BY date DESC
        """)
        existing_data = cur.fetchall()
        conn_dest.close()
        
        # 저장된 데이터 딕셔너리 (code별로 마지막 날짜 시간)
        last_dates = {}
        for date_str, code in existing_data:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            if code not in last_dates or date_obj > last_dates[code]:
                last_dates[code] = date_obj
        
        # 데이터 저장 리스트
        records = []
        
        # 10분당 200건 제한을 위한 큐 (10분 = 600초)
        request_queue = deque(maxlen=200)
        start_time = time.time()
        
        # 2. 각 종목에 대해 저장되지 않은 10분봉 데이터만 조회
        for idx, code in enumerate(all_codes):
            last_date = last_dates.get(code)
            
            print(f"   [{idx+1}/{len(all_codes)}] {code} ({code_to_asset_type[code]})")

            if last_date and last_date.date() == target_date:
                continue
            
            start_date = last_date.strftime("%Y%m%d") if last_date else "20200101"
            cts_date = last_date.strftime("%Y%m%d") if last_date else ""
            cts_time = last_date.strftime("%H%M%S") if last_date else ""

            print(f"       조회 기간: {start_date} ~ {target_date_str}, DB에 저장된 마지막 데이터: {last_date if last_date else '없음'}")
            
            # 10분당 200건 제한 체크
            current_time = time.time()
            if current_time - start_time > 600:  # 10분이 지남
                request_queue.clear()
                start_time = current_time
            while len(request_queue) >= 200:
                time.sleep(1)  # 대기
                current_time = time.time()
                if current_time - start_time > 600:
                    request_queue.clear()
                    start_time = current_time
            
            res = query.t8412(
                shcode=code,
                ncnt=10,    # 10분
                qrycnt=500, # 최대 500건
                nday="0",
                sdate=start_date,
                stime="",
                edate=target_date_str,
                etime="",
                cts_date=cts_date,
                cts_time=cts_time,
                comp_yn="N",  # 압축여부: N (비압축)
                cont=False
            )
            
            request_queue.append((code, current_time))
            
            if res:
                for item in res:
                    item_date = item.get("날짜", "")
                    item_time = item.get("시간", "")
                    if not item_date or not item_time:
                        continue
                    
                    time_int = int(item_time)
                    if not (90000 <= time_int <= 110000):
                        continue
                    
                    formatted_date = f"{item_date[:4]}-{item_date[4:6]}-{item_date[6:]} {item_time[:2]}:{item_time[2:4]}:00"
                    date_obj = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
                    if last_date and date_obj <= last_date:
                        continue
                    
                    asset_type = code_to_asset_type.get(code, "Unknown")
                    
                    open_val = float(item.get("시가", "0").replace(",", ""))
                    close_val = float(item.get("종가", "0").replace(",", ""))
                    
                    records.append((
                        formatted_date, asset_type, code, period, period_value, "open", open_val
                    ))
                    records.append((
                        formatted_date, asset_type, code, period, period_value, "close", close_val
                    ))
            
            # 1초당 1건 제한 (1.1초 대기)
            time.sleep(1.1 - (time.time() - current_time) if time.time() - current_time < 1.1 else 0)
        
        # 3. DB에 저장 (새로운 데이터만)
        if records:
            conn_dest = sqlite3.connect(dest_db_path)
            cur = conn_dest.cursor()
            
            insert_query = """
            INSERT OR REPLACE INTO asset_info 
            (date, asset_type, code, period, period_value, value_type, value)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            
            cur.executemany(insert_query, records)
            conn_dest.commit()
            logging.info(f"[분봉 데이터 저장 완료] 총 {len(records)}건의 새로운 10분봉 데이터 저장 (9시~11시 open/close).")
            
            conn_dest.close()
        else:
            logging.info("[분봉 데이터 저장 완료] 조회된 새로운 데이터가 없습니다.")
        
        if _sessioni_disconnect:
            # 서버 disconnect
            session.disconnect_server()
            print("[종료] 서버 연결 해제.")

    def save_MonthWeeklyDaily_values(self, _src_db_path=None, _dest_db_path=None, _period="daily", _period_value=10, _login_server=None, _sessioni_disconnect=True):
        """
        함수 설명:
        1. invest_items.py (MPAA)의 모든 종목에 대해 10분봉 데이터 (open, close) 조회.
        3. xingAPI 서버 접속부터 데이터 저장까지 수행.
        4. DB: MPAA_donna_min.db의 asset_info 테이블에 저장.
        - date: YYYY-MM-DD HH:MM:SS (봉 시간 포함)
        - asset_type: MPAA의 key (e.g., '국가', '섹터' 등)
        - code: 종목코드
        - period: 'minute'
        - period_value: 10
        - value_type: 'open' 또는 'close'
        - value: 해당 값
        5. 개선: 어제까지 저장된 데이터 확인 후, 오늘(15:30 이후) 또는 어제(15:30 전) 데이터만 추가 조회.
        6. 추가 개선: DB에 저장되지 않은 데이터만 조회하여 추가 (전체 데이터 조회 최소화).
        7. t8412 제한 반영: 1초당 1건, 10분당 200건 제한 준수.
        """
        
        logging.info(f"\n[{_period}]봉 데이터 저장 시작...")

        # 현재 시간 확인 (2025-09-05 05:32 PM KST)
        now = datetime.now()
        cutoff_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
        target_date = now.date() if now >= cutoff_time else (now - timedelta(days=1)).date()
        target_date_str = target_date.strftime("%Y%m%d")

        period_map = {'minute':'분', 'daily':'일', 'weekly':'주', 'monthly':'월'}
        period_str = period_map.get(_period, _period)

        # DB 경로 설정
        src_db_path = _src_db_path if _src_db_path else self.DB_PRICE_DAILY 
        dest_db_path = _dest_db_path if _dest_db_path else self.DB_PRICE_MIN
        
        # MPAA에서 모든 종목 코드와 asset_type 매핑 추출
        code_to_asset_type = {}
        for asset_type, items in MPAA.items():
            for code in items.keys():
                code_to_asset_type[code] = asset_type
        
        all_codes = list(code_to_asset_type.keys())
        logging.info(f"[종목 목록] 총 {len(all_codes)}개 종목 조회 시작.")
        
        # 1. xingAPI 서버 접속 및 로그인
        login_server = _login_server
        crypto_wallet = CRYPTO_WALLET[login_server]
        account_pwd = crypto_wallet["acc_pwd"]

        session = XASession(login_server)
        session.connect_server()
        session.login(crypto_wallet)
        
        if not session.response:
            logging.info("[오류] 로그인 실패.")
            session.disconnect_server()
            return
        
        logging.info("[로그인] 서버 접속 및 로그인 성공.")
        
        period = _period # "daily"
        period_value = _period_value # 10
        
        # XAQuery 인스턴스 생성
        query = XAQuery()
        
        # 기존 데이터 확인 (저장된 날짜와 코드별 마지막 시간)
        if period == "minute":
            conn_dest = sqlite3.connect(dest_db_path)
            cur = conn_dest.cursor()
            cur.execute("""
                SELECT date, code FROM asset_info 
                WHERE period='minute' AND period_value=10 
                ORDER BY date DESC
            """)
        if period == "daily" or period == "weekly" or period == "monthly":
            conn_dest = sqlite3.connect(src_db_path)
            cur = conn_dest.cursor()
            cur.execute(f"""
                SELECT date, code FROM asset_info 
                WHERE period='{period}' 
                ORDER BY date DESC
            """)
        existing_data = cur.fetchall()
        conn_dest.close()
        
        # 저장된 데이터 딕셔너리 (code별로 마지막 날짜 시간)
        last_dates = {}
        for date_str, code in existing_data:
            if period == "daily" or period == "weekly" or period == "monthly":
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            if period == "minute":
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            if code not in last_dates or date_obj > last_dates[code]:
                last_dates[code] = date_obj
        
        # 데이터 저장 리스트
        records = []
        
        # 10분당 200건 제한을 위한 큐 (10분 = 600초)
        request_queue = deque(maxlen=200)
        start_time = time.time()
        
        # 2. 각 종목에 대해 저장되지 않은 10분봉/일봉 데이터만 조회
        for idx, code in enumerate(all_codes):
            last_date = last_dates.get(code)
            
            logging.info(f"   [{idx+1}/{len(all_codes)}] {code} ({code_to_asset_type[code]})")

            if last_date and last_date.date() == target_date:
                continue
            
            start_date = last_date.strftime("%Y%m%d") if last_date else "20200101"
            cts_date = last_date.strftime("%Y%m%d") if last_date else ""
            cts_time = ""
            if period == "minute":
                cts_time = last_date.strftime("%H%M%S") if last_date else ""

            logging.info(f"       조회 기간: {start_date} ~ {target_date_str}, DB에 저장된 마지막 데이터: {last_date if last_date else '없음'}")
            
            # 10분당 200건 제한 체크
            current_time = time.time()
            if current_time - start_time > 600:  # 10분이 지남
                request_queue.clear()
                start_time = current_time

            while len(request_queue) >= 200:
                time.sleep(1)  # 대기
                current_time = time.time()
                if current_time - start_time > 600:
                    request_queue.clear()
                    start_time = current_time
            
            if period == "minute":
                res = query.t8412(
                    shcode=code,
                    ncnt=10,    # 10분
                    qrycnt=500, # 최대 500건
                    nday="0",
                    sdate=start_date,
                    stime="",
                    edate=target_date_str,
                    etime="",
                    cts_date=cts_date,
                    cts_time=cts_time,
                    comp_yn="N",  # 압축여부: N (비압축)
                    cont=False
                )
            if period == "daily" or period == "weekly" or period == "monthly":
                res = query.t8410(
                    shcode=code,
                    gubun=period_str,
                    qrycnt=500,
                    sdate=start_date,
                    edate=target_date_str,
                    cts_date="",
                    comp_yn="N",
                    sujung="Y",
                    cont=False
                )

            request_queue.append((code, current_time))

            if res:
                for item in res:
                    item_date = item.get("날짜", "")
                    item_time = item.get("시간", "")

                    if period == "daily":
                        if not item_date:
                            continue
                        formatted_date = f"{item_date[:4]}-{item_date[4:6]}-{item_date[6:]}"
                        date_obj = datetime.strptime(formatted_date, "%Y-%m-%d")

                    if period == "minute":
                        if not item_date or not item_time:
                            continue
                        time_int = int(item_time)
                        if not (90000 <= time_int <= 110000):
                            continue
                        formatted_date = f"{item_date[:4]}-{item_date[4:6]}-{item_date[6:]} {item_time[:2]}:{item_time[2:4]}:00"
                        date_obj = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
                    
                    if last_date and date_obj <= last_date:
                        continue
                    
                    if period == "daily" or period == "weekly" or period == "monthly":
                        asset_type = code_to_asset_type[code] # code_to_asset_type.get(code, "Unknown")
                    if period == "minute":
                        asset_type = code_to_asset_type.get(code, "Unknown")
                    
                    open_val = float(item.get("시가", "0").replace(",", ""))
                    close_val = float(item.get("종가", "0").replace(",", ""))
                    high_val = float(item.get("고가", "0").replace(",", ""))
                    low_val = float(item.get("저가", "0").replace(",", ""))
                    avg_val = (high_val + low_val) / 2
                    
                    if period == "daily" or period == "weekly" or period == "monthly":
                        records.append((
                            formatted_date, asset_type, code, period, "open", open_val
                        ))
                        records.append((
                            formatted_date, asset_type, code, period, "close", close_val
                        ))
                        records.append((
                            formatted_date, asset_type, code, period, "avg", avg_val
                        ))
                    if period == "minute":
                        records.append((
                            formatted_date, asset_type, code, period, period_value, "open", open_val
                        ))
                        records.append((
                            formatted_date, asset_type, code, period, period_value, "close", close_val
                        ))
                        records.append((
                            formatted_date, asset_type, code, period, period_value, "avg", avg_val
                        ))

            # 1초당 1건 제한 (1.1초 대기)
            time.sleep(1.1 - (time.time() - current_time) if time.time() - current_time < 1.1 else 0)
        
        # 3. DB에 저장 (새로운 데이터만)
        if records:
            if period == "minute":
                conn_dest = sqlite3.connect(dest_db_path)
           
                insert_query = """
                INSERT OR REPLACE INTO asset_info 
                (date, asset_type, code, period, period_value, value_type, value)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """

            if period == "daily" or period == "weekly" or period == "monthly":
                conn_dest = sqlite3.connect(src_db_path)

                insert_query = """
                INSERT OR REPLACE INTO asset_info 
                (date, asset_type, code, period, value_type, value)
                VALUES (?, ?, ?, ?, ?, ?)
                """


            cur = conn_dest.cursor()
            
            cur.executemany(insert_query, records)
            conn_dest.commit()
            logging.info(f"[{_period}봉 데이터 저장 완료] 총 {len(records)}건의 새로운 {period_str}봉 데이터 저장 (9시~11시 open/close).")
            
            conn_dest.close()
        else:
            logging.info(f"[{_period}봉 데이터 저장 완료] 조회된 새로운 데이터가 없습니다.")
        
        if _sessioni_disconnect:
            # 서버 disconnect
            session.disconnect_server()
            logging.info("[종료] 서버 연결 해제.")


# 함수 실행 예시 (직접 호출 시)
if __name__ == "__main__":

    Main(period=None, period_value=None)

