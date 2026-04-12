import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import sqlite3
import sys
from datetime import date, datetime, timedelta
import time
# from MPAA_실제전략평가_Grok_V1_13 import *
from MPAA_실제전략평가_Grok_V1_14 import * # 20251115


# import sqlite3
import logging

# 간단한 logging 설정 (실전은 파일로 기록할 수도 있음)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 상위 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from src.config.invest_items import *

"""
MPAA_strategy
│
├─ __init__()
│   ├─ is_latest_weight_equal_close()    (동기화 확인)
│   ├─ 자산군별_평균모멘텀과스코어()        (평균모멘텀, 모멘텀스코어 계산)
│   ├─ 자산_날짜_종목_순위()                (종목별 순위 선정)
│   ├─ 자산군별_투자비중()                  (자산군별 투자비중 계산)
│   ├─ 자산군별_현금혼합절대평균모멘텀스코어() (현금비중 포함 종목비중)
│   ├─ 전략_수익곡선모멘텀()                 (포트폴리오 수익곡선)
│   └─ 수익곡선모멘텀_지표계산()             (MDD, CAGR 계산/그래프)
│
├─ 자산군별_평균모멘텀과스코어()
│   ├─ get_momentum_score_df_by_asset_type()
│   └─ save_asset_excel()
│
├─ 자산_날짜_종목_순위()
│   ├─ read_rank_from_db()
│   └─ save_rank_to_excel()
│
├─ 자산군별_투자비중()
│   ├─ get_last_date_from_db()
│   ├─ read_weight_from_db_table2()
│   ├─ write_weight_to_db()
│   └─ unique_preserve_order()
│
├─ 전략_수익곡선모멘텀()
│   └─ 평균모멘텀스코어()
│
├─ 전략_총수익률()
│   └─ read_profit_rate_full()
│
└─ 기타 보조 함수들
"""


class MPAA_strategy:
    def __init__(self, mpaa_period=None, 평균이동방법="단순이동평균", 평균이동구간비율=None, 분봉시간=None, 종목선정기준=1/3, 현금비율=0.25, b누적수익곡선적용=False, bGraphDisplay=False):

        start_time = time.time()
        logging.info(f">>>>> MPAA 전략 계산 시작 [mpaa_period:{mpaa_period}, 평균이동방법:{평균이동방법}, 평균이동구간비율:{평균이동구간비율}, 종목선정기준:{종목선정기준}, 현금비율:{현금비율}, b누적수익곡선적용:{b누적수익곡선적용}, bGraphDisplay:{bGraphDisplay}] : {start_time}")

        # 일봉/주봉/월봉 데이터(종가, 시가, 평균가) 가 저장된 데이터베이스
        self.db_price_daily_path = r"D:\_MPAA_Project\MPAA\MPAA_price.db"  # self.db_path = r"D:\_MPAA_Project\MPAA\MPAA_donna_4.db"

        # 분봉(10분봉 9시~11시 시가, 종가) 데이터가 저장된 데이터베이스
        self.db_price_min_path = r"D:\_MPAA_Project\MPAA\MPAA_price_min.db"
        self.db_min_time = 분봉시간 if 분봉시간 is not None else '0910'

        # 종목별 모멘텀/스코어/weight 등이 저장된 데이터베이스
        평균이동구간비율 = 평균이동구간비율 if 평균이동구간비율 is not None else 30
        db_data_path_name = f"D:\_MPAA_Project\MPAA\MPAA_data_{평균이동방법}_{평균이동구간비율}.db"
        src_db_path = r"D:\_MPAA_Project\MPAA\원본_MPAA_data.db"
        dest_db_path = db_data_path_name
        # 위 경로의 파일이 없을 경우 구조를 복사. DB 생성 및 구조 복사 (파일 없을 경우)
        if not os.path.exists(db_data_path_name):
            self.copy_db_schema(src_db_path, dest_db_path)

        self.db_data_path = db_data_path_name        # self.db_data_path = r"D:\_MPAA_Project\MPAA2\MPAA_data.db"

        # 각 전략별 수익률 정보 데이터가 저장된 데이터베이스
        self.db_result_path = r"D:\_MPAA_Project\MPAA\MPAA_result.db"

        self.excel_dir = r"D:\_MPAA_Project\MPAA"

        logging.info(f"    >>>>> DB 경로 설정 완료")   
        logging.info(f"          price_daily    : {self.db_price_daily_path}")   
        logging.info(f"          price_min      : {self.db_price_min_path}")   
        logging.info(f"          data           : {self.db_data_path}")   
        logging.info(f"          result         : {self.db_result_path}")   

        # 1. 주기(period) 문자열 처리 (한글 → 영문)
        mpaa_period = "일" if mpaa_period is None else mpaa_period
        self.period = mpaa_period if mpaa_period else "월"
        period_map = {'일': 'daily', '주': 'weekly', '월': 'monthly'}
        self.period_str = period_map.get(self.period, self.period)

        self.b누적수익곡선적용 = b누적수익곡선적용
        self.excel_save = False
        self.return_full = False

        self.sell = "open"
        self.buy = "avg"

        self.현금비율 = 현금비율
        self.종목선정기준 = 종목선정기준
        self.전체자산_dict = {}
        self.자산군별투자비중 = None  # 필요시 함수에서 할당

        self.평균이동방법 = 평균이동방법
        self.no_of_month = 12
        self.minimum_percent_period = 평균이동구간비율 if 평균이동구간비율 is not None else 30 #100 #30
        self.score_len = 6  # 예시: 월 단위일 때 6개월

        if self.period == "주":
            self.no_of_month = 12 * 4
            self.score_len = 6 * 4
        elif self.period == "일":
            self.no_of_month = 12 * 4 * 5
            self.score_len = 6 * 4 * 5

        self.자산군별_평균모멘텀_dict = {}
        self.자산군별_평균모멘텀스코어_dict = {}
        self.자산군별_종목당최종투자비중_dict = {}
        self.자산군별_월간수익률_dict = {}
        self.전략_투자금_df = {}

        # ============ [개선 포인트 1: 최신 date 동기화 체크] ============
        if self.is_latest_weight_equal_close():
            logging.info("    ----> 자산군 weight와 종가 봉 값의 마지막 날짜가 모두 동일하므로 전략을 계산하지 않고 종료합니다.")
            if bGraphDisplay == False:
                end_time = time.time()
                logging.info(f">>>>> MPAA 전략 계산 종료. 수행 시간: {end_time - start_time:.4f} 초")
                return
            else:
                # mpaa_실제전략평가 = MPAA_Strategy(db_path=self.db_price_daily_path)
                # mpaa_실제전략평가.calculate_S41(strategy='S41_100', period='daily', incremental=True, sell_price_type='open', buy_price_type='avg', partial_sell_ratio=1.0)
                logging.info("    ----> 그러나 bGraphDisplay=True 이므로 그래프는 표시합니다.")
                self.MPAA_전략평가_그래프(분봉시간=self.db_min_time, bGraphDisplay=bGraphDisplay)

                end_time = time.time()
                logging.info(f">>>>> MPAA 전략 계산 종료. 수행 시간: {end_time - start_time:.4f} 초")
                return

        # 자산군별 평균모멘텀과 스코어 계산
        self.자산군별_평균모멘텀_dict, self.자산군별_평균모멘텀스코어_dict = self.자산군별_평균모멘텀과스코어(
            db_path=self.db_price_daily_path,
            db_data_path=self.db_data_path,
            period=self.period_str,
            no_of_month=self.no_of_month,
            min_percent=self.minimum_percent_period, #30, #100,
            mean_method=self.평균이동방법,
            excel_save=self.excel_save,
            excel_dir=self.excel_dir,
            return_full=False
        )

        # 자산군별 종목 순위 계산
        self.자산_날짜_종목_순위_dict = self.자산_날짜_종목_순위(
            종목선정기준=self.종목선정기준, 
            db_path=self.db_price_daily_path,  # db_path=r"D:/_MPAA_Project/MPAA/MPAA_price.db",
            db_data_path=self.db_data_path,  # db_path=r"D:/_MPAA_Project/MPAA/MPAA_data.db",
            table_name="asset_info", 
            period_str=self.period_str,
            excel_save=self.excel_save,
            return_full=self.return_full
        )

        # 자산군별 투자 비중 계산
        self.자산군별_투자비중_df = self.자산군별_투자비중(
            db_path=self.db_data_path, 
            period=self.period_str,
            현금비율=self.현금비율,
            excel_save=self.excel_save,
            return_full=self.return_full
        )

        # 자산군별 종목당 최종 투자 비중 계산
        self.자산군별_종목당최종투자비중_dict = self.자산군별_현금혼합절대평균모멘텀스코어(
            db_path=self.db_price_daily_path, 
            db_data_path=self.db_data_path,
            period=self.period_str,
            excel_save=self.excel_save,
            return_full=self.return_full,
        )

        # (옵션) 그래프 및 수익곡선 처리
        if bGraphDisplay:
            # mpaa_실제전략평가 = MPAA_Strategy(db_price_daily_path=None, db_price_min_path=None, db_data_path=None, db_result_path=None)
            # mpaa_실제전략평가.calculate_S41(strategy='S41_100', period='daily', incremental=True, sell_price_type='open', buy_price_type='avg', partial_sell_ratio=1.0)
            # mpaa_실제전략평가.calculate_S41_V2(strategy='S41_30_min0910_DBnew2', period='daily', incremental=True, start_date=None, end_date=None, sell_price_type='open', buy_price_type='avg', partial_sell_ratio=1.0)
            self.MPAA_전략평가_그래프(분봉시간=self.db_min_time, bGraphDisplay=bGraphDisplay)

        end_time = time.time()
        logging.info(f">>>>> MPAA 전략 계산 종료. 수행 시간: {end_time - start_time:.4f} 초\n")

    def MPAA_전략평가_그래프(self, 분봉시간=None, bGraphDisplay=False):
        """
        """
        min_time = 분봉시간 if 분봉시간 is not None else '0910'
        # 인스턴스 생성
        mpaa_실제전략평가 = MPAA_Strategy(
            db_price_daily_path=self.db_price_daily_path, 
            db_price_min_path=self.db_price_min_path, 
            db_data_path=self.db_data_path, 
            db_result_path=self.db_result_path
        )
        # 실제 전략 평가 및 그래프 표시
        strategy_name = f"S41_{self.minimum_percent_period}_min{min_time}_{self.평균이동방법}"

        mpaa_실제전략평가.calculate_S41_V2(
            strategy=strategy_name, #'S41_50_min0910_지수이동평균', 
            period='daily', 
            incremental=True, 
            start_date=None, 
            end_date=None, 
            sell_price_type='open', 
            buy_price_type='avg', 
            partial_sell_ratio=1.0,
            bGraphDisplay=bGraphDisplay
        )

    def copy_db_schema(self, original_db_path, new_db_path):
        """
        원본 DB의 구조(스키마)만 복사해서 새로운 DB를 만듦
        - original_db_path: 원본 DB 파일 경로 (예: 'MPAA_donna.db')
        - new_db_path: 새 DB 파일 경로 (예: 'MPAA_donna2.db')
        """
        import sqlite3
        
        # 원본 DB 연결
        orig_conn = sqlite3.connect(original_db_path)
        orig_cursor = orig_conn.cursor()
        
        # 새 DB 연결 (파일이 없으면 자동 생성)
        new_conn = sqlite3.connect(new_db_path)
        new_cursor = new_conn.cursor()
        
        # 원본의 모든 테이블/인덱스/뷰 등의 CREATE 문 추출
        orig_cursor.execute("SELECT name, type, sql FROM sqlite_master WHERE sql NOT NULL")
        for name, obj_type, sql in orig_cursor.fetchall():
            # CREATE 문 실행 (데이터는 복사 안 함)
            new_cursor.execute(sql)
        
        # 변경 저장하고 연결 끊기
        new_conn.commit()
        orig_conn.close()
        new_conn.close()

        logging.info(f"구조 복사 완료! {original_db_path} -> {new_db_path}")

    def is_latest_weight_equal_close(self):
        """
        period=self.period_str 일 때, 
        self.db_data_path 의 asset_info 테이블에서 value_type=weight, 
        self.db_price_daily_path      의 asset_info 테이블에서 value_type=close의 code별 마지막 date가 모두 같으면 True, 아니면 False
        """
        try:
            conn = sqlite3.connect(self.db_data_path)
            cursor = conn.cursor()

            # value_type=weight의 code별 마지막 date
            cursor.execute("""
                SELECT code, MAX(date)
                FROM asset_info
                WHERE period=? AND value_type='weight'
                GROUP BY code
            """, (self.period_str,))
            weight_last_dates = dict(cursor.fetchall())
            conn.close()

            conn = sqlite3.connect(self.db_price_daily_path)
            cursor = conn.cursor()

            # value_type=close의 code별 마지막 date
            cursor.execute("""
                SELECT code, MAX(date)
                FROM asset_info
                WHERE period=? AND value_type='close'
                GROUP BY code
            """, (self.period_str,))
            close_last_dates = dict(cursor.fetchall())
            conn.close()
        except Exception as e:
            logging.warning(f"DB에서 날짜 비교 중 오류 발생: {e}")
            return False  # 예외 발생시 실행하도록 처리

        # 두 그룹 모두 있는 code만 비교
        codes = set(weight_last_dates.keys()) & set(close_last_dates.keys())
        if not codes:
            logging.info("weight와 close의 공통 코드가 없습니다. 전략 실행합니다.")
            return False

        for code in codes:
            if weight_last_dates[code] != close_last_dates[code]:
                logging.info(f"[{code}] weight 마지막 date({weight_last_dates[code]}) ≠ close 마지막 date({close_last_dates[code]})")
                return False
        return True

    def invest_jongmok_rate(self):
        invest_dict = self.자산군별_종목당최종투자비중_dict
        final_dict = {}
        index_list = next(iter(invest_dict.values())).index

        for idx in index_list:
            row_result = {}
            for key in invest_dict:
                df_invest = invest_dict[key]
                if idx in df_invest.index:
                    invest_row = df_invest.loc[idx]
                    for col, val in invest_row.items():
                        if val != 0:
                            row_result[col] = val
            final_dict[idx] = row_result

        return final_dict, invest_dict

    def invest_jongmok_rate_from_db(self, db_data_path=None, period=None):
        """
        이 함수는 main_mpaa_db_251117_01_Strategy_S41 에서 사용됩니다.
        DB에서 자산군별 weight 데이터를 읽어와서 마지막 2개 날짜의 종목별 투자 비중 DataFrame을 반환합니다.
        """
        # db_path = self.db_price_daily_path        # db_path = r"D:\_MPAA_Project\MPAA\MPAA_donna_4.db"
        db_path = db_data_path if db_data_path is not None else self.db_data_path

        logging.info(f"    >>>>> invest_jongmok_rate_from_db 시작 : {db_path}, period: {period}")
        
        period_map = {'일': 'daily', '주': 'weekly', '월': 'monthly'}
        period_str = period_map.get(period, period)
        if period is None:
            period_str = 'daily'

        start_time = time.time()
        conn = sqlite3.connect(db_path)

        # [1] 마지막 2개 날짜만 추출
        sql_dates = """
            SELECT DISTINCT date
            FROM asset_info
            WHERE period = ? AND value_type = 'weight'
            ORDER BY date ASC
        """
        dates = pd.read_sql_query(sql_dates, conn, params=(period_str,))

        if len(dates) == 0:
            logging.warning("    >>>>> 데이터가 없습니다.")
            conn.close()
            return None

        elif len(dates) == 1:
            # 데이터가 1개만 있을 때
            date_last = pd.to_datetime(dates['date'].iloc[0])

            # 실제 데이터 추출
            sql_main = """
                SELECT date, asset_type, code, value
                FROM asset_info
                WHERE period = ?
                AND value_type = 'weight'
                AND date = ?
            """
            df = pd.read_sql_query(sql_main, conn, params=(period_str, date_last.strftime('%Y-%m-%d')))
            conn.close()
            df['date'] = pd.to_datetime(df['date'])

            # value > 0만 사용
            df_last = df[df['value'] > 0]
            df_last_pivot = df_last.pivot_table(index='date', columns='code', values='value').fillna(0)

            # 하루 전 date 만들기
            date_last_1 = date_last - timedelta(days=1)
            zero_row = pd.DataFrame(
                0,
                index=[date_last_1],
                columns=df_last_pivot.columns
            )

            # 합치기
            target_invest_jongmok_df = pd.concat([zero_row, df_last_pivot])
            target_invest_jongmok_df.index.name = 'date'

        else:
            date_last_1 = dates['date'].iloc[-2]
            date_last = dates['date'].iloc[-1]

            # 두 날짜 데이터만 추출
            sql_main = """
                SELECT date, asset_type, code, value
                FROM asset_info
                WHERE period = ?
                AND value_type = 'weight'
                AND (date = ? OR date = ?)
            """
            df = pd.read_sql_query(sql_main, conn, params=(period_str, date_last_1, date_last))
            conn.close()
            df['date'] = pd.to_datetime(df['date'])

            # 날짜별로 value > 0만 사용
            df_last_1 = df[(df['date'] == pd.to_datetime(date_last_1)) & (df['value'] > 0)]
            df_last = df[(df['date'] == pd.to_datetime(date_last)) & (df['value'] > 0)]

            df_last_1_pivot = df_last_1.pivot_table(index='date', columns='code', values='value').fillna(0)
            df_last_pivot = df_last.pivot_table(index='date', columns='code', values='value').fillna(0)

            # 합집합 기준 컬럼 정렬
            all_codes = sorted(set(df_last_1_pivot.columns).union(set(df_last_pivot.columns)))
            df_last_1_pivot = df_last_1_pivot.reindex(columns=all_codes, fill_value=0)
            df_last_pivot = df_last_pivot.reindex(columns=all_codes, fill_value=0)

            target_invest_jongmok_df = pd.concat([df_last_1_pivot, df_last_pivot])
            target_invest_jongmok_df.index.name = 'date'

        end_time = time.time()
        logging.info(f"    >>>>> invest_jongmok_rate_from_db 함수 수행 시간: {end_time - start_time:.4f} 초")

        return target_invest_jongmok_df

    def 전략_수익곡선모멘텀(self, score_len, no_of_month):
        start_time = time.time()
        print(f"    >>>>> 전략 수익곡선모멘텀 계산 시작[전략_수익곡선모멘텀()]")
        cash_monthly_profit_df = self.자산군별_월간수익률_dict['현금']
        mpaa_cumulative_profit_df = pd.DataFrame(self.전략_총수익률_df['월별누적수익율'], index=self.전략_총수익률_df.index)
        mpaa_average_momentum_score_df = self.평균모멘텀스코어(mpaa_cumulative_profit_df, score_len=score_len, momentum_len=no_of_month)
        mpaa_average_momentum_score_df = mpaa_average_momentum_score_df.shift(1)
        mpaa_monthly_profit_df = pd.DataFrame(self.전략_총수익률_df['월간수익률'], index=self.전략_총수익률_df.index)

        mpaa_cumulative_profit_df = pd.DataFrame(
            (mpaa_average_momentum_score_df.values * mpaa_monthly_profit_df.values + (1 - mpaa_average_momentum_score_df.values) * cash_monthly_profit_df),
            index=cash_monthly_profit_df.index
        )
        mpaa_cumulative_profit_df = mpaa_cumulative_profit_df.cumprod().dropna()
        mpaa_cumulative_profit_df.columns = ["월별누적수익율"]

        self.MPAA_누적수익률_df = mpaa_cumulative_profit_df
        end_time = time.time()
        print(f"    >>>>> 전략 수익곡선모멘텀 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
        return mpaa_cumulative_profit_df

    def 수익곡선모멘텀_지표계산(self, 기준데이터=None, 전략결과=None):
        start_time = time.time()
        logging.info(">>>>> 수익곡선모멘텀_지표계산 시작[수익곡선모멘텀_지표계산()]")
        start_date = "2002-10-18"
        end_date = "2025-02-28"

        def get_code_series(db_path, code, period='daily', value_type='close'):
            conn = sqlite3.connect(db_path)
            query = """
                SELECT date, value
                FROM asset_info
                WHERE code=? AND period=? AND value_type=?
                ORDER BY date
            """
            df = pd.read_sql_query(query, conn, params=(code, period, value_type))
            conn.close()
            df['date'] = pd.to_datetime(df['date'])
            series = pd.Series(df['value'].values, index=df['date'])
            series.name = code
            return series
        기준데이터 = get_code_series(db_path=self.db_price_daily_path, code='069500', period='daily', value_type='close')

        def get_strategy_result_series(db_path, asset_type='월별누적수익율', period='daily', value_type='profit_rate'):
            conn = sqlite3.connect(db_path)
            query = """
                SELECT date, value
                FROM asset_info2
                WHERE asset_type=? AND period=? AND value_type=?
                ORDER BY date
            """
            df = pd.read_sql_query(query, conn, params=(asset_type, period, value_type))
            conn.close()
            df['date'] = pd.to_datetime(df['date'])
            series = pd.Series(df['value'].values, index=df['date'])
            series.name = asset_type
            return series

        전략결과 = get_strategy_result_series(db_path=self.db_price_daily_path, asset_type='월별누적수익율', period='daily', value_type='profit_rate')

        b = 기준데이터 / 기준데이터.iloc[0]
        c = pd.concat([전략결과, b], axis=1)
        c.columns = ['포트폴리오', '코스피']

        if start_date is not None:
            c = c.loc[start_date:]
        if end_date is not None:
            c = c.loc[:end_date]
        c = c.dropna()

        최대하락 = c["포트폴리오"].rolling(min_periods=1, window=500).max()
        당월하락 = c["포트폴리오"] / 최대하락 - 1.0
        최대하락폭 = 당월하락.rolling(min_periods=1, window=500).min()

        if False: # self.b전략테스트 이 변수를 사용할 경우
            if self.b전략테스트 == False:
                start_date_val = c.index.min()
                end_date_val = c.index.max()
                start_date_val = pd.to_datetime(start_date_val)
                end_date_val = pd.to_datetime(end_date_val)
                days = (end_date_val - start_date_val).days
                투자기간 = days / 365.25
            else:
                투자기간 = len(c.index) / 12
        else:
            start_date_val = c.index.min()
            end_date_val = c.index.max()
            start_date_val = pd.to_datetime(start_date_val)
            end_date_val = pd.to_datetime(end_date_val)
            days = (end_date_val - start_date_val).days
            투자기간 = days / 365.25

        mdd_value = 최대하락폭.min() * 100
        cagr_value = c["포트폴리오"].iloc[-1] ** (1 / 투자기간) * 100 - 100

        logging.info(f"     [전략 결과] 매도 [{self.sell}] : 매수 [{self.buy}],     MDD: {mdd_value:.2f}%,     CAGR: {cagr_value:.2f}%")

        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(18, 14), gridspec_kw={'height_ratios': [4, 1]})
        (c / c.iloc[0]).plot(ax=ax1)
        ax1.set_title("수익곡선")
        ax1.set_ylabel("정규화 수익")
        ax1.grid(True)
        ax2.plot(c.index, 당월하락, linestyle='dotted', label="당월하락")
        ax2.plot(c.index, 최대하락폭, linestyle='dotted', color='red', label="최대하락폭")
        ax2.set_title("MDD 시각화")
        ax2.set_ylabel("수익률")
        ax2.legend()
        ax2.grid(True)
        end_time = time.time()
        logging.info(f">>>>> 수익곡선모멘텀_지표계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
        plt.tight_layout()
        plt.show()

    def get_last_date_from_db(self, db_path, table, period, value_type):
        conn = sqlite3.connect(db_path)
        query = f"""
            SELECT MAX(date) as last_date
            FROM {table}
            WHERE period = ? AND value_type = ?
        """
        row = conn.execute(query, (period, value_type)).fetchone()
        conn.close()
        return row[0] if row and row[0] else None

    def read_weight_from_db_table2(self, db_path, period, asset_types):
        # asset_info2에서 weight 데이터를 읽어 date-index, asset_type-column df로 변환
        conn = sqlite3.connect(db_path)
        query = f"""
            SELECT date, asset_type, value
            FROM asset_info2
            WHERE period = ? AND value_type = 'weight'
        """
        df = pd.read_sql_query(query, conn, params=(period,))
        conn.close()
        if df.empty:
            return pd.DataFrame()
        # Pivot: date-index, asset_type-column
        df['date'] = pd.to_datetime(df['date'])
        df_pivot = df.pivot(index='date', columns='asset_type', values='value')
        # 컬럼 정렬
        df_pivot = df_pivot.reindex(columns=asset_types)
        return df_pivot

    def write_weight_to_db(self, db_path, period, new_weight_df):
        # asset_info2에 weight 데이터 추가 (update or insert)
        conn = sqlite3.connect(db_path)
        rows = []
        for date, row in new_weight_df.iterrows():
            for asset_type, value in row.items():
                rows.append((str(date), asset_type, 'weight', period, value))
        conn.executemany("""
            INSERT OR REPLACE INTO asset_info2 (date, asset_type, value_type, period, value)
            VALUES (?, ?, ?, ?, ?)
        """, rows)
        conn.commit()
        conn.close()

    def unique_preserve_order(self, lst):
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]

    def 자산군별_투자비중(
        self,
        db_path=r"D:\_MPAA_Project\MPAA\MPAA_data.db",     # db_data_path=r"D:\_MPAA_Project\MPAA\MPAA_data.db",
        period='daily',
        현금비율=0.25,
        excel_save=True,
        return_full=True
    ):
        """
        자산군별 투자 비중을 계산합니다.
        1) 최신 weight 상태면 즉시 기존 데이터 반환
        2) print 대신 logging 사용
        3) 엑셀저장/DB저장 포함
        """
        start_time = time.time()
        logging.info(">>>>> 자산군별 투자비중 계산 시작[자산군별_투자비중()]")

        period_str = period if period else self.period_str
        현금비율 = 현금비율 if 현금비율 is not None else self.현금비율

        # 자산군 리스트: MPAA는 클래스 변수나 글로벌 딕셔너리로 가정
        asset_types = list(MPAA.keys())

        # 1. DB에서 가장 마지막 날짜 확인
        last_weight_date = self.get_last_date_from_db(db_path, 'asset_info2', period_str, 'weight')
        last_momentum_date = self.get_last_date_from_db(db_path, 'asset_info', period_str, 'momentum_score')
        last_rank_date = self.get_last_date_from_db(db_path, 'asset_info', period_str, 'rank')

        logging.info(f"    ----> 마지막 weight date: {last_weight_date}, momentum_score: {last_momentum_date}, rank: {last_rank_date}")

        # 2. 최신 데이터 상태면 즉시 기존 weight 반환 (성능 개선)
        if last_momentum_date == last_weight_date and last_weight_date is not None:
            logging.info("    ----> weight가 최신 상태입니다. 추가 계산 없이 기존 데이터 반환.")
            if return_full:
                full_weight_df = self.read_weight_from_db_table2(db_path, period_str, self.unique_preserve_order(asset_types + ['현금']))
                end_time = time.time()
                logging.info(f">>>>> 자산군별 투자비중 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return full_weight_df
            end_time = time.time()
            logging.info(f">>>>> 자산군별 투자비중 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return pd.DataFrame()

        # 3. momentum_score/rank 데이터 읽기 (필요 date만)
        conn = sqlite3.connect(db_path)
        date_filter = ""
        params = [period_str]
        if last_weight_date:
            date_filter = "AND date > ?"
            params.append(last_weight_date)
        mom_query = f"""
            SELECT date, asset_type, code, value
            FROM asset_info
            WHERE period = ? AND value_type = 'momentum_score' {date_filter}
        """
        mom_df = pd.read_sql_query(mom_query, conn, params=params)
        rank_query = f"""
            SELECT date, asset_type, code, value
            FROM asset_info
            WHERE period = ? AND value_type = 'rank' {date_filter}
        """
        rank_df = pd.read_sql_query(rank_query, conn, params=params)
        conn.close()

        # 4. 추가 계산 불필요(신규 없음) 시 기존 데이터 반환
        if mom_df.empty or rank_df.empty:
            logging.info("    ----> 자산군별_투자비중을 추가 계산할 momentum_score/rank 데이터가 없습니다.")
            if excel_save:
                full_weight_df = self.read_weight_from_db_table2(db_path, period_str, self.unique_preserve_order(asset_types + ['현금']))
                file_name = f"자산군별_투자비중_{self.period}.xlsx"
                with pd.ExcelWriter(file_name) as writer:
                    full_weight_df.to_excel(writer, sheet_name="weight")
            if return_full:
                full_weight_df = self.read_weight_from_db_table2(db_path, period_str, self.unique_preserve_order(asset_types + ['현금']))
                end_time = time.time()
                logging.info(f">>>>> 자산군별 투자비중 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return full_weight_df
            end_time = time.time()
            logging.info(f">>>>> 자산군별 투자비중 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return pd.DataFrame()

        # 5. 자산군/종목별로 피벗 변환 및 비중 계산
        new_weight_dict = {}
        for asset in asset_types:
            mom = mom_df[mom_df['asset_type'] == asset]
            rank = rank_df[rank_df['asset_type'] == asset]
            if mom.empty or rank.empty:
                continue
            mom_pivot = mom.pivot(index='date', columns='code', values='value').sort_index()
            rank_pivot = rank.pivot(index='date', columns='code', values='value').sort_index()
            computed = mom_pivot * rank_pivot
            new_weight_dict[asset] = computed

        # 6. 기준 인덱스(date) 집합 만들기
        all_dates = set()
        for df in new_weight_dict.values():
            all_dates |= set(df.index)
        new_index = sorted(all_dates)
        available_df = pd.DataFrame(False, index=new_index, columns=asset_types)
        for asset in asset_types:
            if asset in new_weight_dict:
                asset_available = new_weight_dict[asset].gt(0).any(axis=1)
                available_df[asset] = asset_available.reindex(new_index, fill_value=False)

        # 7. 기본 배분 비율 설정
        weights = pd.DataFrame(0.0, index=new_index, columns=asset_types)
        all_available_mask = available_df.all(axis=1)
        if len(asset_types) > 1:
            nonbond_count = len(asset_types) - 1
            weights.loc[all_available_mask, "채권"] = 0.5
            for asset in asset_types:
                if asset != "채권":
                    weights.loc[all_available_mask, asset] = 0.5 / nonbond_count
        else:
            weights.loc[all_available_mask, :] = 1.0

        not_all_mask = ~all_available_mask
        available_counts = available_df.loc[not_all_mask].sum(axis=1)
        weights_rule2 = available_df.loc[not_all_mask].div(available_counts, axis=0).fillna(0.0)
        weights.loc[not_all_mask] = weights_rule2

        # 8. 현금 비율 반영
        weights = weights * (1 - 현금비율)
        non_cash_total = weights.sum(axis=1)
        cash_col = pd.Series(np.where(non_cash_total > 0, 현금비율, 1.0), index=new_index)
        computed_weights_new = weights.copy()
        computed_weights_new["현금"] = cash_col

        # 9. 컬럼 순서 고정 및 중복 제거
        col_order = self.unique_preserve_order(asset_types + ["현금"])
        computed_weights_new = computed_weights_new[col_order]

        # 10. DB에 신규 데이터 저장
        self.write_weight_to_db(db_path, period_str, computed_weights_new)

        # 11. 엑셀 저장(최신 전체 데이터)
        if excel_save:
            full_weight_df = self.read_weight_from_db_table2(db_path, period_str, col_order)
            file_name = f"자산군별_투자비중_{self.period}.xlsx"
            with pd.ExcelWriter(file_name) as writer:
                full_weight_df.to_excel(writer, sheet_name="weight")

        logging.info(f"    ----> 신규 데이터({len(new_index)})건을 추가했습니다.")
        end_time = time.time()
        logging.info(f">>>>> 자산군별 투자비중 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")

        if return_full:
            return full_weight_df
        return computed_weights_new

    def read_rank_from_db(self, db_path, period_str):
        """DB에서 rank 데이터를 읽어 asset별 DataFrame 딕셔너리로 변환"""
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("""
            SELECT * FROM asset_info
            WHERE period=? AND value_type='rank'
        """, conn, params=(period_str,))
        conn.close()
        result = {}
        if df.empty:
            return result
        for asset in df['asset_type'].unique():
            df_sub = df[df['asset_type'] == asset]
            pivoted = df_sub.pivot(index='date', columns='code', values='value')
            pivoted.index = pd.to_datetime(pivoted.index)
            result[asset] = pivoted.sort_index()
        return result

    def 자산_날짜_종목_순위(
        self,
        종목선정기준=0.3,
        db_path=None, #r"D:/_MPAA_Project/MPAA/MPAA_donna.db",
        db_data_path=None, #r"D:/_MPAA_Project/MPAA/MPAA_data.db",  
        table_name="asset_info",
        period_str=None,
        excel_save=True,
        return_full=True
        ):
        logger = logging.getLogger("자산_날짜_종목_순위")
        import time
        start_time = time.time()
        logger.info(">>>>> 자산군별 종목 순위 계산 시작[자산_날짜_종목_순위()]")

        if period_str is None:
            period_str = self.period_str

        # conn = sqlite3.connect(db_path)
        conn = sqlite3.connect(db_data_path)

        # asset_types, codes 준비
        asset_types = list(MPAA.keys())
        asset_type_code_dict = {
            asset: sorted(list(codes.keys()))
            for asset, codes in MPAA.items()
        }

        # 1. 각 자산군별로 마지막 rank/momentum 날짜 쿼리
        last_rank_dict = {}
        last_momentum_dict = {}
        all_synced = True

        for asset in asset_types:
            last_rank = conn.execute(
                f"SELECT MAX(date) FROM {table_name} WHERE period=? AND value_type='rank' AND asset_type=?",
                (period_str, asset)
            ).fetchone()[0]
            last_rank_dict[asset] = last_rank
            last_momentum = conn.execute(
                f"SELECT MAX(date) FROM {table_name} WHERE period=? AND value_type='momentum' AND asset_type=?",
                (period_str, asset)
            ).fetchone()[0]
            last_momentum_dict[asset] = last_momentum
            if last_rank != last_momentum:
                all_synced = False

        logger.info(f"    -----> last_rank_dict: {last_rank_dict}")
        logger.info(f"    -----> last_momentum_dict: {last_momentum_dict}")

        if all_synced:
            logger.info("    -----> 모든 자산군의 rank와 momentum의 마지막 날짜가 일치합니다. 함수 종료!")
            conn.close()
            end_time = time.time()
            logger.info(f">>>>> 자산군별 종목 순위 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return None  # 이미 최신 상태

        순위결과 = {}
        신규추가_존재 = False
        전체_need_dates = {}

        for asset in asset_types:
            codes = asset_type_code_dict[asset]
            last_rank = last_rank_dict[asset]
            last_momentum = last_momentum_dict[asset]

            if not last_momentum:
                logger.warning(f"    -----> momentum 데이터가 없습니다. [{asset}]")
                continue

            # 2. rank에 없는 date만 선별하여 momentum 데이터만 읽기
            if last_rank:
                query_dates = f"""
                    SELECT DISTINCT date
                    FROM {table_name}
                    WHERE period=? AND value_type='momentum' AND asset_type=? AND date > ?
                    ORDER BY date
                """
                need_dates = [r[0] for r in conn.execute(query_dates, (period_str, asset, last_rank)).fetchall()]
            else:
                query_dates = f"""
                    SELECT DISTINCT date
                    FROM {table_name}
                    WHERE period=? AND value_type='momentum' AND asset_type=? 
                    ORDER BY date
                """
                need_dates = [r[0] for r in conn.execute(query_dates, (period_str, asset)).fetchall()]
            전체_need_dates[asset] = need_dates

            if not need_dates:
                logger.info(f"    -----> [{asset}] : 새로운 데이터가 없습니다.")
                순위결과[asset] = pd.DataFrame(columns=codes)
                continue
            else:
                신규추가_존재 = True

            # 3. 필요한 날짜만 포함하는 momentum 데이터만 읽기
            momentum_query = f"""
                SELECT * FROM {table_name}
                WHERE period=? AND value_type='momentum' AND asset_type=? AND date IN ({','.join(['?']*len(need_dates))})
                ORDER BY date
            """
            params = [period_str, asset] + need_dates
            df_mom = pd.read_sql_query(momentum_query, conn, params=params)
            if df_mom.empty:
                순위결과[asset] = pd.DataFrame(columns=codes)
                continue

            df_mom['date'] = pd.to_datetime(df_mom['date'])
            pivot = df_mom.pivot(index='date', columns='code', values='value').sort_index()
            pivot = pivot.reindex(columns=codes, fill_value=0)  # 자산군별 기준 코드 집합 사용

            # 4. rank 계산 (벡터화)
            tmp = pivot.mask(pivot == 0)
            mom_rank_df = tmp.rank(axis=1, ascending=False, method='min')
            종목수_series = (pivot != 0).sum(axis=1).apply(
                lambda cnt: int(round(cnt * 종목선정기준)) if cnt > 0 else 1
            )
            종목수_series = 종목수_series.apply(lambda x: x if x >= 1 else 1)
            new_selection_df = ((mom_rank_df.le(종목수_series, axis=0)) & (pivot != 0)).astype(int)
            new_selection_df = new_selection_df.reindex(columns=codes, fill_value=0)

            # 5. 신규 rank만 결과에 저장
            순위결과[asset] = new_selection_df

            # 6. 신규 rank만 DB에 UPSERT
            rows = []
            for d, row in new_selection_df.iterrows():
                for c, v in row.items():
                    rows.append((str(d.date()), asset, period_str, "rank", c, float(v)))
            if rows:
                conn.executemany(
                    f"""INSERT OR REPLACE INTO {table_name} 
                    (date, asset_type, period, value_type, code, value) 
                    VALUES (?, ?, ?, ?, ?, ?)""", rows
                )

        conn.commit()

        # 7. 엑셀 저장 or 전체 데이터 반환 (옵션, 필요시 전체를 DB에서 읽음)
        if excel_save or return_full:
            full_rank_df = self.read_rank_from_db(db_data_path, period_str)
            if excel_save:
                self.save_rank_to_excel(full_rank_df, db_path, period_str)
                logger.info(f"    -----> 엑셀 파일 저장 완료: 자산_날짜_종목_순위_dict_{self.period}.xlsx")
            if return_full:
                conn.close()
                end_time = time.time()
                logger.info(f">>>>> 자산군별 종목 순위 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return full_rank_df
            else:
                결과 = {}
                for k, v in 순위결과.items():
                    if not v.empty:
                        rows = [r for r in v.index if str(r) in 전체_need_dates.get(k, [])]
                        결과[k] = v.loc[rows]
                conn.close()
                end_time = time.time()
                logger.info(f">>>>> 자산군별 종목 순위 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return 결과
        else:
            conn.close()
            end_time = time.time()
            logger.info(f">>>>> 자산군별 종목 순위 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return 순위결과

    def save_rank_to_excel(self, rank_dict, db_path, period_str='daily'):
        파일경로 = f"자산_날짜_종목_순위_dict_{self.period}.xlsx"

        with pd.ExcelWriter(파일경로) as writer:
            for 자산, df in rank_dict.items():
                conn_excel = sqlite3.connect(db_path)
                codes = conn_excel.execute(
                    f"SELECT DISTINCT code FROM asset_info WHERE asset_type=? AND value_type='close' AND period=?",
                    (자산, period_str)
                ).fetchall()
                codes = sorted([str(c[0]) for c in codes])
                conn_excel.close()

                df = df.reindex(columns=codes, fill_value=0)
                df.to_excel(writer, sheet_name=자산)
                nan_counts = df.isna().sum()
                nan_cols = nan_counts[nan_counts > 0]
                if not nan_cols.empty:
                    print(f"    >>>>> [엑셀 저장 경고] {자산} - NaN(빈칸) 있는 컬럼: {list(nan_cols.index)}")
                else:
                    print(f"    >>>>> [엑셀 저장] {자산} : 모든 컬럼 결측 없음")
        print(f"    >>>>> 엑셀 파일 저장 완료: {파일경로}")

    def get_momentum_score_df_by_asset_type(
        self,
        db_path,
        db_data_path,
        period='daily'
    ):
        import sqlite3
        import pandas as pd

        # conn = sqlite3.connect(db_path)

        asset_types = list(MPAA.keys())
        momentum_dict = {}
        score_dict = {}

        for asset in asset_types:
            # 2. 해당 자산군의 close unique date, code 확보
            conn = sqlite3.connect(db_path)
            df_close = pd.read_sql_query(
                """
                SELECT DISTINCT date, code
                FROM asset_info
                WHERE period = ? AND value_type = 'close' AND asset_type = ?
                """, conn, params=(period, asset)
            )
            conn.close()

            # 3. momentum만 별도로 쿼리
            conn = sqlite3.connect(db_data_path)
            df_mom = pd.read_sql_query(
                """
                SELECT date, code, value
                FROM asset_info
                WHERE period = ? AND value_type = 'momentum' AND asset_type = ?
                """, conn, params=(period, asset)
            )
            # pivot (index=date, columns=code, 값=momentum), fill 0
            mom_df = df_close.merge(df_mom, on=['date', 'code'], how='left')
            mom_df = mom_df.pivot(index='date', columns='code', values='value').fillna(0)
            momentum_dict[asset] = mom_df

            # 4. momentum_score만 별도로 쿼리
            df_score = pd.read_sql_query(
                """
                SELECT date, code, value
                FROM asset_info
                WHERE period = ? AND value_type = 'momentum_score' AND asset_type = ?
                """, conn, params=(period, asset)
            )
            score_df = df_close.merge(df_score, on=['date', 'code'], how='left')
            score_df = score_df.pivot(index='date', columns='code', values='value').fillna(0)
            score_dict[asset] = score_df

        conn.close()
        return momentum_dict, score_dict

    def save_asset_excel(self, all_momentum, all_score, out_dir, period):
        """
        자산군별 모멘텀/스코어 딕셔너리를 각각 엑셀로 저장 (sheet별 자산군)
        """
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        momentum_path = os.path.join(out_dir, f"자산군별_평균모멘텀_dict_{period}.xlsx")
        score_path = os.path.join(out_dir, f"자산군별_평균모멘텀스코어_dict_{period}.xlsx")
        
        # momentum 저장
        with pd.ExcelWriter(momentum_path) as writer:
            for asset, df_sub in all_momentum.items():
                if df_sub.empty:
                    print(f"    >>>>> [WARNING] 모멘텀 DataFrame이 비어있음: asset={asset}")
                    continue
                df_sub = df_sub.sort_index(ascending=True)
                print(f"    >>>>> [SAVE] 모멘텀: {asset}, shape={df_sub.shape}")
                df_sub.to_excel(writer, sheet_name=str(asset))
        print(f"    >>>>> 모멘텀 엑셀 저장 완료: {momentum_path}")

        # score 저장
        with pd.ExcelWriter(score_path) as writer:
            for asset, df_sub in all_score.items():
                if df_sub.empty:
                    print(f"    >>>>> [WARNING] 모멘텀스코어 DataFrame이 비어있음: asset={asset}")
                    continue
                df_sub = df_sub.sort_index(ascending=True)
                print(f"    >>>>> [SAVE] 모멘텀스코어: {asset}, shape={df_sub.shape}")
                df_sub.to_excel(writer, sheet_name=str(asset))
        print(f"    >>>>> 모멘텀스코어 엑셀 저장 완료: {score_path}")

    def 자산군별_평균모멘텀과스코어0(
        self,
        db_path,
        db_data_path,
        period,
        no_of_month=12,
        mean_method='단순이동평균',
        excel_save=False,
        excel_dir=None,
        return_full=False
        ):
        """
        자산군별 평균모멘텀과 모멘텀스코어를 계산해서 DB에 저장하고,
        필요시 엑셀 파일로 저장하는 함수입니다.

        데이터의 날짜 정합성을 먼저 검사해서,
        문제가 있으면 바로 함수가 종료됩니다.

        Args:
            db_path (str): 자산의 가격 데이터 SQLite DB 경로
            db_data_path (str): 자산의 가격에 대한 weight, momentum/score 등의 데이터 DB 경로
            period (str): 'monthly', 'weekly', 'daily' 등
            no_of_month (int): 모멘텀 계산 구간 (예: 12)
            mean_method (str): '단순이동평균' 또는 '지수이동평균'
            excel_save (bool): 엑셀 저장 여부
            excel_dir (str): 엑셀 저장 디렉터리
            return_full (bool): 전체 데이터프레임 반환 여부

        Returns:
            (momentum_df, score_df) 또는 ({}, {})
        """
        start_time = time.time()
        logging.info(">>>>> 자산군별_평균모멘텀/스코어 계산 시작")

        conn = sqlite3.connect(db_path)

        # 1. close 데이터 로드 및 정합성 검사
        code_list = [code for asset_group in MPAA.values() for code in asset_group.keys()]
        placeholders = ','.join(['?'] * len(code_list))
        query = f"""
        SELECT date, code, asset_type, value
        FROM asset_info
        WHERE period = ? AND value_type = 'close'
        AND code IN ({placeholders})
        """
        params = [period] + code_list
        df_close = pd.read_sql_query(query, conn, params=params)
        # df_close = pd.read_sql_query(
        #     "SELECT date, code, asset_type, value FROM asset_info WHERE period = ? AND value_type = 'close'",
        #     conn, params=(period,)
        # )
        if df_close.empty:
            logging.error("        -----> DB에 close 데이터가 없습니다.")
            conn.close()
            return {}, {}

        # 각 종목(code)별 마지막 날짜 구하기
        df_close['date'] = pd.to_datetime(df_close['date'])
        close_dates = df_close.groupby('code')['date'].max()

        # close의 모든 code의 마지막 날짜가 동일해야만 통과
        if close_dates.nunique() != 1:
            logging.error("        -----> close 데이터의 각 code별 마지막 날짜가 일치하지 않습니다. close 데이터부터 갱신하세요!")
            conn.close()
            raise ValueError("        -----> close 데이터 정합성 오류: 모든 code의 date가 동일해야 합니다.")

        close_last_date = close_dates.iloc[0]

        # 2. momentum/momentum_score 데이터 로드 및 정합성 검사
        # df_momentum = pd.read_sql_query(
        #     "SELECT code, MAX(date) as last_date FROM asset_info WHERE period=? AND value_type='momentum' GROUP BY code",
        #     conn, params=(period,)
        # )
        # df_score = pd.read_sql_query(
        #     "SELECT code, MAX(date) as last_date FROM asset_info WHERE period=? AND value_type='momentum_score' GROUP BY code",
        #     conn, params=(period,)
        # )

        # momentum 데이터 로드
        conn = sqlite3.connect(db_data_path)
        query_momentum = f"""
        SELECT code, MAX(date) as last_date
        FROM asset_info
        WHERE period = ?
        AND value_type = 'momentum'
        AND code IN ({placeholders})
        GROUP BY code
        """
        params_momentum = [period] + code_list
        df_momentum = pd.read_sql_query(query_momentum, conn, params=params_momentum)

        # momentum_score 데이터 로드
        query_score = f"""
        SELECT code, MAX(date) as last_date
        FROM asset_info
        WHERE period = ?
        AND value_type = 'momentum_score'
        AND code IN ({placeholders})
        GROUP BY code
        """
        params_score = [period] + code_list
        df_score = pd.read_sql_query(query_score, conn, params=params_score)

        # 둘 다 데이터가 없을 수도 있음(최초 실행시)
        if (not df_momentum.empty) and (not df_score.empty):
            # code별 마지막 날짜가 모두 동일해야만 통과
            if df_momentum['last_date'].nunique() != 1 or df_score['last_date'].nunique() != 1:
                logging.error("        -----> momentum 또는 momentum_score의 code별 마지막 날짜가 일치하지 않습니다. 데이터 정합성 오류!")
                conn.close()
                raise ValueError("        -----> momentum, momentum_score 데이터 정합성 오류: 모든 code의 date가 동일해야 합니다.")

            momentum_last_date = pd.to_datetime(df_momentum['last_date'].iloc[0])
            score_last_date = pd.to_datetime(df_score['last_date'].iloc[0])

            # close, momentum, score 세 날짜가 모두 같으면 즉시 종료
            if (momentum_last_date == close_last_date) and (score_last_date == close_last_date):
                logging.info("        -----> 모든 데이터가 최신입니다. 추가 계산 불필요하여 함수 종료합니다.")
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f}초\n")
                return {}, {}

        # 3. 모멘텀/스코어 계산 구간 설정
        code_asset_map = df_close.groupby('code')['asset_type'].first().to_dict()
        all_dates = sorted(df_close['date'].unique())
        all_codes = sorted(df_close['code'].unique())

        # 기존 마지막 모멘텀/스코어 날짜 이후부터 계산
        if (not df_momentum.empty) and (not df_score.empty):
            calc_start_date = max(pd.to_datetime(df_momentum['last_date'].iloc[0]), pd.to_datetime(df_score['last_date'].iloc[0]))
        elif not df_momentum.empty:
            calc_start_date = pd.to_datetime(df_momentum['last_date'].iloc[0])
        elif not df_score.empty:
            calc_start_date = pd.to_datetime(df_score['last_date'].iloc[0])
        else:
            calc_start_date = None

        all_dates_series = pd.Series(all_dates)
        if calc_start_date is not None:
            min_date_idx = all_dates_series.searchsorted(calc_start_date)
            need_start_idx = max(0, min_date_idx - no_of_month)
            date_needed = all_dates_series[need_start_idx:]
        else:
            date_needed = all_dates_series

        if len(date_needed) <= no_of_month:
            logging.warning("        -----> 모멘텀/스코어 계산에 필요한 데이터 구간이 충분하지 않습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        date_min = date_needed.iloc[0].strftime('%Y-%m-%d')
        date_max = date_needed.iloc[-1].strftime('%Y-%m-%d')
        logging.info(f"        -----> ▶️ 계산 대상 구간: {date_needed.iloc[no_of_month].date()} ~ {date_needed.iloc[-1].date()}, 총 {len(date_needed)-no_of_month}일")

        # 4. 피벗 변환 및 필요한 구간만 추출
        df_close_sel = df_close[(df_close['date'] >= pd.to_datetime(date_min)) & (df_close['date'] <= pd.to_datetime(date_max))]
        if df_close_sel.empty:
            logging.warning("        -----> 해당 구간의 close 데이터가 없습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        df_pivot = df_close_sel.pivot_table(index='date', columns='code', values='value').sort_index()
        df_pivot = df_pivot.reindex(index=pd.to_datetime(date_needed), columns=all_codes)

        # 5. 모멘텀/스코어 벡터 연산
        momentum_list = [df_pivot / df_pivot.shift(i) for i in range(1, no_of_month + 1)]
        score_list = [(df_pivot / df_pivot.shift(i) > 1).astype(int) for i in range(1, no_of_month + 1)]
        누적모멘텀 = sum(momentum_list)
        누적스코어 = sum(score_list)

        if mean_method == '단순이동평균':
            계산_모멘텀 = 누적모멘텀 / no_of_month
        elif mean_method == '지수이동평균':
            계산_모멘텀 = 누적모멘텀.ewm(span=no_of_month).mean()
        else:
            raise ValueError("        -----> mean_method는 '단순이동평균' 또는 '지수이동평균'만 지원합니다.")

        계산_스코어 = 누적스코어 / no_of_month
        계산_모멘텀.iloc[:no_of_month, :] = np.nan
        계산_스코어.iloc[:no_of_month, :] = np.nan

        # 6. 결과 대상 날짜 추출
        target_dates = date_needed[no_of_month:]
        if calc_start_date is not None:
            target_dates = target_dates[target_dates > calc_start_date]
        if len(target_dates) == 0:
            logging.warning("        -----> 계산할 target_dates가 없습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        # 7. DB insert 준비 (필요 대상만 long-form)
        multi_index = pd.MultiIndex.from_product([target_dates, all_codes], names=['date', 'code'])
        df_base = pd.DataFrame(index=multi_index).reset_index()
        df_base['asset_type'] = df_base['code'].map(code_asset_map)
        df_base['period'] = period

        insert_rows = []
        for value_type, df_result in [('momentum', 계산_모멘텀), ('momentum_score', 계산_스코어)]:
            df_long = df_result.loc[target_dates].stack().reset_index()
            df_long.columns = ['date', 'code', 'value']
            df_merged = pd.merge(df_base, df_long, on=['date', 'code'], how='left')
            df_merged['value_type'] = value_type
            df_merged['value'] = df_merged['value'].fillna(0)
            df_merged = df_merged[['date', 'asset_type', 'code', 'period', 'value_type', 'value']]
            insert_rows.append(df_merged)
        total_insert = pd.concat(insert_rows, ignore_index=True)

        # 8. DB에 insert
        conn = sqlite3.connect(db_data_path)
        if not total_insert.empty:
            total_insert['date'] = total_insert['date'].astype(str)
            total_insert.to_sql("asset_info", conn, if_exists='append', index=False, chunksize=500)
            logging.info(f"        -----> 모멘텀/스코어 DB 저장 완료. 총 {len(total_insert)} rows insert.")

        excel_save = True

        # 9. 결과 반환 및 엑셀 저장
        if excel_save or return_full:
            all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
            if excel_save:
                out_dir = excel_dir or "."
                self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
            conn.close()
            end_time = time.time()
            logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
            return all_momentum, all_score
        else:
            conn.close()
            end_time = time.time()
            logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
            return {}, {}

    def 자산군별_평균모멘텀과스코어(
        self,
        db_path,
        db_data_path,
        period,
        no_of_month=12,
        min_percent=100,  # 새 변수! 최소 % (예: 50 = no_of_month의 50% 이상 과거 데이터부터 계산)
        mean_method='단순이동평균',
        excel_save=False,
        excel_dir=None,
        return_full=False
        ):
        """
        자산군별 평균모멘텀과 모멘텀스코어를 계산해서 DB에 저장하고,
        필요시 엑셀 파일로 저장하는 함수입니다.

        데이터의 날짜 정합성을 먼저 검사해서,
        문제가 있으면 바로 함수가 종료됩니다.

        Args:
            db_path (str): 자산의 가격 데이터 SQLite DB 경로
            db_data_path (str): 자산의 가격에 대한 weight, momentum/score 등의 데이터 DB 경로
            period (str): 'monthly', 'weekly', 'daily' 등
            no_of_month (int): 모멘텀 계산 구간 (예: 12)
            min_percent (int): 최소 계산 시작 % (예: 50 = no_of_month의 50% 이상 과거 데이터부터 평균 계산. 기본 50)
            mean_method (str): '단순이동평균' 또는 '지수이동평균'
            excel_save (bool): 엑셀 저장 여부
            excel_dir (str): 엑셀 저장 디렉터리
            return_full (bool): 전체 데이터프레임 반환 여부

        Returns:
            (momentum_df, score_df) 또는 ({}, {})
        """
        import numpy as np
        import pandas as pd
        from datetime import datetime
        import time
        import logging
        import sqlite3

        start_time = time.time()
        logging.info(">>>>> 자산군별_평균모멘텀/스코어 계산 시작")

        conn = sqlite3.connect(db_path)

        # 1. close 데이터 로드 및 정합성 검사
        code_list = [code for asset_group in MPAA.values() for code in asset_group.keys()]
        placeholders = ','.join(['?'] * len(code_list))
        query = f"""
        SELECT date, code, asset_type, value
        FROM asset_info
        WHERE period = ? AND value_type = 'close'
        AND code IN ({placeholders})
        """
        params = [period] + code_list
        df_close = pd.read_sql_query(query, conn, params=params)
        if df_close.empty:
            logging.error("        -----> DB에 close 데이터가 없습니다.")
            conn.close()
            return {}, {}

        # 각 종목(code)별 마지막 날짜 구하기
        df_close['date'] = pd.to_datetime(df_close['date'])
        close_dates = df_close.groupby('code')['date'].max()

        # close의 모든 code의 마지막 날짜가 동일해야만 통과
        if close_dates.nunique() != 1:
            logging.error("        -----> close 데이터의 각 code별 마지막 날짜가 일치하지 않습니다. close 데이터부터 갱신하세요!")
            conn.close()
            raise ValueError("        -----> close 데이터 정합성 오류: 모든 code의 date가 동일해야 합니다.")

        close_last_date = close_dates.iloc[0]

        # 2. momentum/momentum_score 데이터 로드 및 정합성 검사
        # momentum 데이터 로드
        conn = sqlite3.connect(db_data_path)
        query_momentum = f"""
        SELECT code, MAX(date) as last_date
        FROM asset_info
        WHERE period = ?
        AND value_type = 'momentum'
        AND code IN ({placeholders})
        GROUP BY code
        """
        params_momentum = [period] + code_list
        df_momentum = pd.read_sql_query(query_momentum, conn, params=params_momentum)

        # momentum_score 데이터 로드
        query_score = f"""
        SELECT code, MAX(date) as last_date
        FROM asset_info
        WHERE period = ?
        AND value_type = 'momentum_score'
        AND code IN ({placeholders})
        GROUP BY code
        """
        params_score = [period] + code_list
        df_score = pd.read_sql_query(query_score, conn, params=params_score)

        # 둘 다 데이터가 없을 수도 있음(최초 실행시)
        if (not df_momentum.empty) and (not df_score.empty):
            # code별 마지막 날짜가 모두 동일해야만 통과
            if df_momentum['last_date'].nunique() != 1 or df_score['last_date'].nunique() != 1:
                logging.error("        -----> momentum 또는 momentum_score의 code별 마지막 날짜가 일치하지 않습니다. 데이터 정합성 오류!")
                conn.close()
                raise ValueError("        -----> momentum, momentum_score 데이터 정합성 오류: 모든 code의 date가 동일해야 합니다.")

            momentum_last_date = pd.to_datetime(df_momentum['last_date'].iloc[0])
            score_last_date = pd.to_datetime(df_score['last_date'].iloc[0])

            # close, momentum, score 세 날짜가 모두 같으면 즉시 종료
            if (momentum_last_date == close_last_date) and (score_last_date == close_last_date):
                logging.info("        -----> 모든 데이터가 최신입니다. 추가 계산 불필요하여 함수 종료합니다.")
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f}초\n")
                return {}, {}

        # 3. 모멘텀/스코어 계산 구간 설정
        code_asset_map = df_close.groupby('code')['asset_type'].first().to_dict()
        all_dates = sorted(df_close['date'].unique())
        all_codes = sorted(df_close['code'].unique())

        # 기존 마지막 모멘텀/스코어 날짜 이후부터 계산
        if (not df_momentum.empty) and (not df_score.empty):
            calc_start_date = max(pd.to_datetime(df_momentum['last_date'].iloc[0]), pd.to_datetime(df_score['last_date'].iloc[0]))
        elif not df_momentum.empty:
            calc_start_date = pd.to_datetime(df_momentum['last_date'].iloc[0])
        elif not df_score.empty:
            calc_start_date = pd.to_datetime(df_score['last_date'].iloc[0])
        else:
            calc_start_date = None

        all_dates_series = pd.Series(all_dates)
        if calc_start_date is not None:
            min_date_idx = all_dates_series.searchsorted(calc_start_date)
            need_start_idx = max(0, min_date_idx - no_of_month)
            date_needed = all_dates_series[need_start_idx:]
        else:
            date_needed = all_dates_series

        if len(date_needed) <= no_of_month:
            logging.warning("        -----> 모멘텀/스코어 계산에 필요한 데이터 구간이 충분하지 않습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        date_min = date_needed.iloc[0].strftime('%Y-%m-%d')
        date_max = date_needed.iloc[-1].strftime('%Y-%m-%d')
        min_data_count = int(no_of_month * (min_percent / 100.0))  # 최소 과거 데이터 수 (예: 10*0.5=5)
        logging.info(f"        -----> ▶️ 계산 대상 구간: {date_needed.iloc[no_of_month].date()} ~ {date_needed.iloc[-1].date()}, 총 {len(date_needed)-no_of_month}일. 최소 과거 데이터: {min_data_count}개 ({min_percent}%)")

        # 4. 피벗 변환 및 필요한 구간만 추출
        df_close_sel = df_close[(df_close['date'] >= pd.to_datetime(date_min)) & (df_close['date'] <= pd.to_datetime(date_max))]
        if df_close_sel.empty:
            logging.warning("        -----> 해당 구간의 close 데이터가 없습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        df_pivot = df_close_sel.pivot_table(index='date', columns='code', values='value').sort_index()
        df_pivot = df_pivot.reindex(index=pd.to_datetime(date_needed), columns=all_codes)

        # 5. 빠른 모멘텀/스코어 벡터 연산 (NumPy 방식! min_percent 적용)
        # 모멘텀 계산: 동적 평균 (min_percent 이상 과거 데이터부터)
        def 빠른_모멘텀_계산(df_pivot, no_of_month, min_percent, mean_method):
            prices = df_pivot.values  # (m, n) 배열
            m, n = prices.shape
            max_period = min(no_of_month, m)
            min_data_count = int(no_of_month * (min_percent / 100.0))  # 최소 과거 수
            
            momentum = np.full((m, n), np.nan)
            for col in range(n):  # 각 종목별
                col_prices = prices[:, col]
                past_prices = np.full((m, max_period), np.nan)
                for i in range(1, max_period + 1):
                    if i < m:
                        past_prices[i:, i-1] = col_prices[:-i]
                
                current_prices = col_prices[:, np.newaxis]
                col_momentum = current_prices / past_prices  # (m, max_period)
                
                # 동적 평균: NaN 아닌 개수만큼, 하지만 min_data_count 이상일 때만!
                valid_counts = np.sum(~np.isnan(col_momentum), axis=1)
                # min_data_count 이상일 때만 계산, 아니면 NaN 유지
                mask = valid_counts >= min_data_count
                col_avg = np.full(m, np.nan)
                where_mask = mask & (valid_counts > 0)
                col_sum = np.nansum(col_momentum, axis=1)
                col_avg[where_mask] = col_sum[where_mask] / valid_counts[where_mask]
                
                momentum[:, col] = col_avg
            
            result_df = pd.DataFrame(momentum, index=df_pivot.index, columns=df_pivot.columns)
            if mean_method == '지수이동평균':
                result_df = result_df.ewm(span=no_of_month).mean()
            result_df.iloc[:no_of_month] = np.nan  # 초기 NaN (추가 안전)
            return result_df

        # 스코어 계산: (모멘텀 >1) 개수 / 과거 수 (min_percent 적용)
        def 빠른_스코어_계산(df_pivot, no_of_month, min_percent):
            prices = df_pivot.values
            m, n = prices.shape
            max_period = min(no_of_month, m)
            min_data_count = int(no_of_month * (min_percent / 100.0))  # 최소 과거 수
            
            score = np.full((m, n), np.nan)
            for col in range(n):
                col_prices = prices[:, col]
                past_prices = np.full((m, max_period), np.nan)
                for i in range(1, max_period + 1):
                    if i < m:
                        past_prices[i:, i-1] = col_prices[:-i]
                
                current_prices = col_prices[:, np.newaxis]
                col_score = (current_prices / past_prices > 1).astype(int)  # 1 or 0 (m, max_period)
                
                # 동적 평균: 합 / 개수, min_data_count 이상일 때만!
                valid_counts = np.sum(~np.isnan(col_score), axis=1)
                mask = valid_counts >= min_data_count
                col_avg = np.full(m, np.nan)
                where_mask = mask & (valid_counts > 0)
                col_sum = np.nansum(col_score, axis=1)
                col_avg[where_mask] = col_sum[where_mask] / valid_counts[where_mask]
                
                score[:, col] = col_avg
            
            result_df = pd.DataFrame(score, index=df_pivot.index, columns=df_pivot.columns)
            result_df.iloc[:no_of_month] = np.nan  # 초기 NaN
            return result_df

        # 계산 실행!
        계산_모멘텀 = 빠른_모멘텀_계산(df_pivot, no_of_month, min_percent, mean_method)
        계산_스코어 = 빠른_스코어_계산(df_pivot, no_of_month, min_percent)

        # 6. 결과 대상 날짜 추출
        target_dates = date_needed[no_of_month:]
        if calc_start_date is not None:
            target_dates = target_dates[target_dates > calc_start_date]
        if len(target_dates) == 0:
            logging.warning("        -----> 계산할 target_dates가 없습니다.")
            if return_full or excel_save:
                all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
                if excel_save:
                    out_dir = excel_dir or "."
                    self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
                return all_momentum, all_score
            else:
                conn.close()
                return {}, {}

        # 7. DB insert 준비 (필요 대상만 long-form)
        multi_index = pd.MultiIndex.from_product([target_dates, all_codes], names=['date', 'code'])
        df_base = pd.DataFrame(index=multi_index).reset_index()
        df_base['asset_type'] = df_base['code'].map(code_asset_map)
        df_base['period'] = period

        insert_rows = []
        for value_type, df_result in [('momentum', 계산_모멘텀), ('momentum_score', 계산_스코어)]:
            df_long = df_result.loc[target_dates].stack().reset_index()
            df_long.columns = ['date', 'code', 'value']
            df_merged = pd.merge(df_base, df_long, on=['date', 'code'], how='left')
            df_merged['value_type'] = value_type
            df_merged['value'] = df_merged['value'].fillna(0)
            df_merged = df_merged[['date', 'asset_type', 'code', 'period', 'value_type', 'value']]
            insert_rows.append(df_merged)
        total_insert = pd.concat(insert_rows, ignore_index=True)

        # 8. DB에 insert
        conn = sqlite3.connect(db_data_path)
        if not total_insert.empty:
            total_insert['date'] = total_insert['date'].astype(str)
            total_insert.to_sql("asset_info", conn, if_exists='append', index=False, chunksize=500)
            logging.info(f"        -----> 모멘텀/스코어 DB 저장 완료. 총 {len(total_insert)} rows insert.")

        # 9. 결과 반환 및 엑셀 저장
        if excel_save or return_full:
            all_momentum, all_score = self.get_momentum_score_df_by_asset_type(db_path=db_path, db_data_path=db_data_path, period=period)
            if excel_save:
                out_dir = excel_dir or "."
                self.save_asset_excel(all_momentum, all_score, out_dir, self.period)
            conn.close()
            end_time = time.time()
            logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
            return all_momentum, all_score
        else:
            conn.close()
            end_time = time.time()
            logging.info(f">>>>> 자산군별_평균모멘텀/스코어 계산 종료. 수행 시간: {end_time - start_time:.2f} 초\n")
            return {}, {}

    def 전략_총수익률(
        self,
        db_path,
        period=None,
        excel_save=False,
        excel_path=None,
        return_full=True
    ):
        """
        - asset_info.value_type='close'에서 asset_type 동적 추출
        - weight는 반드시 target_start_date 이전 날짜부터 select(shift(1) 대응)
        - 월별누적수익율은 DB에 저장된 마지막값부터 이어서 for-loop로 곱셈(정확)
        """

        logging.info(">>>>> 전략 총수익률 계산 시작[전략_총수익률()]")

        start_time = time.time()
        period_str = period if period else self.period_str
        conn = sqlite3.connect(db_path)

        # (0) 집계 대상 asset_type 동적 추출
        asset_types = list(MPAA.keys())
        logging.debug(f"[DEBUG] 집계 대상 asset_type: {asset_types}")

        # (1) asset_info2: profit_rate 마지막 날짜
        last_profit2_date = pd.read_sql_query(
            "SELECT MAX(date) AS date FROM asset_info2 WHERE period = ? AND value_type = 'profit_rate'",
            conn, params=(period_str,)
        )["date"][0]

        # (2) asset_info: weight 마지막 날짜
        last_weight_date = pd.read_sql_query(
            "SELECT MAX(date) AS date FROM asset_info WHERE period = ? AND value_type = 'weight'",
            conn, params=(period_str,)
        )["date"][0]

        logging.debug(f"    ----> [DEBUG] last_profit2_date: {last_profit2_date}, last_weight_date: {last_weight_date}")

        need_calc = False
        target_start_date = None
        if (last_weight_date is not None) and (
            (last_profit2_date is None) or (last_weight_date > last_profit2_date)
        ):
            need_calc = True
            target_start_date = last_profit2_date

        # 3. 추가 계산 필요 없는 경우: 전체 profit_rate 데이터 반환/저장
        if not need_calc:
            logging.info("    ----> 신규 계산 필요 없음. (DB가 최신임)")
            if excel_save:
                df = self.read_profit_rate_full(conn, period_str, asset_types)
                if not excel_path:
                    excel_path = f"전략_총수익률_df_{self.period}.xlsx"
                with pd.ExcelWriter(excel_path) as writer:
                    df.to_excel(writer, sheet_name='총수익률')
                logging.info(f"    ----> [DEBUG] 엑셀 저장 완료: {excel_path}")
            if return_full:
                if not excel_save:
                    df = self.read_profit_rate_full(conn, period_str, asset_types)
                end_time = time.time()
                logging.info(f">>>>> 전략 총수익률 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                conn.close()
                return df
            else:
                end_time = time.time()
                logging.info(f">>>>> 전략 총수익률 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                conn.close()
                return {}

        # 4. weight: 반드시 target_start_date의 이전 날짜부터 읽음 (shift(1) 보정)
        if target_start_date is None:
            weight = pd.read_sql_query(
                "SELECT * FROM asset_info WHERE period = ? AND value_type = 'weight'",
                conn, params=(period_str,)
            )
        else:
            prev_date_row = pd.read_sql_query(
                "SELECT date FROM asset_info WHERE period = ? AND value_type = 'weight' AND date < ? ORDER BY date DESC LIMIT 1",
                conn, params=(period_str, target_start_date)
            )
            if not prev_date_row.empty:
                prev_date = prev_date_row["date"][0]
                weight = pd.read_sql_query(
                    "SELECT * FROM asset_info WHERE period = ? AND value_type = 'weight' AND date >= ?",
                    conn, params=(period_str, prev_date)
                )
            else:
                weight = pd.read_sql_query(
                    "SELECT * FROM asset_info WHERE period = ? AND value_type = 'weight' AND date >= ?",
                    conn, params=(period_str, target_start_date)
                )
        if weight.empty:
            logging.error("    ----> [ERROR] 추가 weight 데이터가 없습니다.")
            conn.close()
            return {}

        # asset_type별, date x code DataFrame 생성
        weight_dict = {}
        for asset in asset_types:
            df = weight[weight['asset_type'] == asset]
            if df.empty:
                continue
            df_pivot = df.pivot(index='date', columns='code', values='value').sort_index()
            weight_dict[asset] = df_pivot

        # profit_rate1도 code별로 존재(없으면 0)
        if target_start_date is None:
            profit1 = pd.read_sql_query(
                "SELECT * FROM asset_info WHERE period = ? AND value_type = 'profit_rate'",
                conn, params=(period_str,)
            )
        else:
            profit1 = pd.read_sql_query(
                "SELECT * FROM asset_info WHERE period = ? AND value_type = 'profit_rate' AND date >= ?",
                conn, params=(period_str, target_start_date)
            )
        profit_dict = {}
        if not profit1.empty:
            for asset in asset_types:
                df = profit1[profit1['asset_type'] == asset]
                if df.empty:
                    continue
                df_pivot = df.pivot(index='date', columns='code', values='value').sort_index()
                profit_dict[asset] = df_pivot

        # 5. 월간수익률 계산
        result_df = {}
        for asset in weight_dict:
            profit_df = profit_dict.get(asset, pd.DataFrame(0, index=weight_dict[asset].index, columns=weight_dict[asset].columns))
            w = weight_dict[asset].shift(1)  # shift(1): 월초 기준
            result = w * profit_df
            row_sum = result.sum(axis=1)
            row_sum = row_sum.reindex(weight_dict[asset].index, fill_value=np.nan)
            result_df[asset] = row_sum

        result_df = pd.DataFrame(result_df)
        result_df['월간수익률'] = result_df[asset_types].sum(axis=1)
        result_df['월간수익률'] = result_df['월간수익률'].replace(0, np.nan)

        # === for-loop로 월별누적수익율 정확 계산 ===
        if target_start_date is not None:
            # DB에서 target_start_date의 월별누적수익율 값 1row만 select
            last_cum_row = pd.read_sql_query(
                """
                SELECT value FROM asset_info2
                WHERE period = ? AND value_type = 'profit_rate'
                AND asset_type = '월별누적수익율' AND date = ?
                """,
                conn, params=(period_str, target_start_date)
            )
            if not last_cum_row.empty and not pd.isna(last_cum_row['value'].iloc[0]):
                last_cum_value = last_cum_row['value'].iloc[0]
            else:
                last_cum_value = 1.0

            result_df_to_save = result_df[result_df.index > target_start_date].copy()
            월간수익률 = result_df_to_save['월간수익률'].values
            월별누적수익율 = []
            prev = last_cum_value
            for v in 월간수익률:
                if np.isnan(v):
                    월별누적수익율.append(np.nan)
                else:
                    prev = prev * v
                    월별누적수익율.append(prev)
            result_df_to_save['월별누적수익율'] = 월별누적수익율
        else:
            result_df_to_save = result_df
            result_df_to_save['월별누적수익율'] = result_df_to_save['월간수익률'].cumprod(skipna=True)

        result_df_to_save = result_df_to_save.replace(0, np.nan)

        # 6. 신규 계산 데이터만 asset_info2에 저장 (누적/월간 컬럼 포함)
        for date, row in result_df_to_save.iterrows():
            for asset in result_df_to_save.columns:
                value = row[asset]
                conn.execute(
                    "INSERT OR REPLACE INTO asset_info2 (date, asset_type, period, value_type, value) VALUES (?, ?, ?, 'profit_rate', ?)",
                    (date, asset, period_str, value)
                )
        conn.commit()

        # 7. 전체 profit_rate 데이터 read/엑셀저장/반환
        if excel_save:
            df = self.read_profit_rate_full(conn, period_str, asset_types)
            if not excel_path:
                excel_path = f"전략_총수익률_df_{self.period}.xlsx"
            with pd.ExcelWriter(excel_path) as writer:
                df.to_excel(writer, sheet_name='총수익률')
            logging.info(f"    ----> [DEBUG] 엑셀 저장 완료: {excel_path}")

        if return_full:
            if not excel_save:
                df = self.read_profit_rate_full(conn, period_str, asset_types)
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 전략 총수익률 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return df
        else:
            conn.close()
            end_time = time.time()
            logging.info(f">>>>> 전략 총수익률 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
            return result_df_to_save

    # (공통) 전체 profit_rate 읽기 함수 (asset_type 동적 정렬)
    def read_profit_rate_full(self, conn, period_str, asset_types):

        df = pd.read_sql_query(
            "SELECT date, asset_type, value FROM asset_info2 WHERE period = ? AND value_type = 'profit_rate'",
            conn, params=(period_str,)
        )
        if df.empty:
            return pd.DataFrame()
        # 원하는 컬럼 순서(동적으로 뽑은 asset_types + 월간/누적 컬럼)
        col_order = asset_types + ["월간수익률", "월별누적수익율"]
        df_pivot = df.pivot(index='date', columns='asset_type', values='value').sort_index()
        col_order = [c for c in col_order if c in df_pivot.columns]
        return df_pivot[col_order]

    # --- 공통 DB 읽기 함수 ---

    # (공통) asset_type별로 sheet로 엑셀 저장
    def save_weight_dict_to_excel(self, weight_dict, file_path):
        with pd.ExcelWriter(file_path) as writer:
            for asset, df in weight_dict.items():
                # date가 컬럼명으로 저장되도록 index_label 지정
                df.to_excel(writer, sheet_name=str(asset)[:30], index=True, index_label='date')

    def 자산군별_현금혼합절대평균모멘텀스코어(self, db_path, db_data_path, period=None, excel_save=False, excel_path=None, return_full=True):
        """
        - DB에서 (momentum_score, rank, weight) 데이터의 마지막 날짜 확인
        - 필요한 날짜만 minimal read 후 계산 및 DB 저장
        - 자산군 투자비중을 '선정 종목 수'로 나누어 선정 종목에 균등분배
        - 신규 계산/저장 대상이 없다면, 엑셀/리턴 플래그에 따라 전체 데이터 읽기
        """
        logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 시작")
        start_time = time.time()
        period_str = period if period else self.period_str
        asset_types = list(MPAA.keys())

        conn0 = sqlite3.connect(db_path)

        # with문으로 connection 관리
        with sqlite3.connect(db_data_path) as conn:
            def last_date(value_type, table='asset_info'):
                q = f"SELECT asset_type, MAX(date) FROM {table} WHERE period = ? AND value_type = ? GROUP BY asset_type"
                return dict(conn.execute(q, (period_str, value_type)).fetchall())

            last_weight2_date = last_date('weight', table='asset_info2')
            last_mom_date = last_date('momentum_score')
            last_rank_date = last_date('rank')
            last_weight_date = last_date('weight')

            # (1-1) 함수 최상단에서 날짜 비교 후, 즉시 종료 처리
            if (
                set(last_weight_date.values()) == set(last_mom_date.values())
                and len(last_weight_date) == len(last_mom_date)
                and last_weight_date and last_mom_date
            ):
                end_time = time.time()    
                logging.info("    ----> [자산군별_현금혼합절대평균모멘텀스코어] weight와 mom 날짜가 모두 동일하여 계산을 생략합니다.")
                logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return {}

            # 신규 데이터 날짜 선별
            keys_by_asset = {}
            for asset in asset_types:
                lw2 = last_weight2_date.get(asset, None)
                lm = last_mom_date.get(asset, None)
                lr = last_rank_date.get(asset, None)
                lw = last_weight_date.get(asset, None)

                base_date = lw if lw else "1900-01-01"
                mom_dates = pd.read_sql_query(
                    "SELECT DISTINCT date FROM asset_info WHERE period = ? AND value_type = 'momentum_score' AND asset_type = ? AND date > ?",
                    conn, params=(period_str, asset, base_date)
                )['date'].tolist()
                rank_dates = pd.read_sql_query(
                    "SELECT DISTINCT date FROM asset_info WHERE period = ? AND value_type = 'rank' AND asset_type = ? AND date > ?",
                    conn, params=(period_str, asset, base_date)
                )['date'].tolist()
                valid_dates = sorted(list(set(mom_dates) & set(rank_dates)))
                if valid_dates:
                    keys_by_asset[asset] = valid_dates

            신규추가_존재 = any(len(v) > 0 for v in keys_by_asset.values())

            if not 신규추가_존재:
                logging.info("    ----> 모든 asset에서 신규 데이터가 없습니다.")
                result_dict2 = {}
                if excel_save or return_full:
                    if excel_save:
                        result_dict2 = self.get_all_weight_from_db(conn0=conn0, conn=conn, period_str=period_str)
                        if not excel_path:
                            excel_path = f"자산군별_종목당최종투자비중_dict_{self.period}.xlsx"
                        self.save_weight_dict_to_excel(result_dict2, excel_path)
                        logging.info(f"    ----> 엑셀 파일로 저장 완료: {excel_path}")
                    if return_full:
                        if not excel_save:
                            result_dict2 = self.get_all_weight_from_db(conn0=conn0, conn=conn, period_str=period_str)
                        end_time = time.time()
                        logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                        return result_dict2
                    else:
                        end_time = time.time()
                        logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                        return {}
                else:
                    end_time = time.time()
                    logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                    return {}

            # 1) 기존 방식(반복문/for문)
            def legacy_weight_calc(momentum_dict, rank_dict, weight2_dict):
                weight_dict = {}
                for asset in keys_by_asset:
                    if asset == '현금':
                        continue
                    mom = momentum_dict.get(asset)
                    rank = rank_dict.get(asset)
                    w2 = weight2_dict.get(asset)
                    if mom is None or rank is None or w2 is None:
                        continue

                    dates = sorted(list(set(mom.index) & set(rank.index) & set(w2.index)))
                    codes = sorted(list(set(mom.columns) & set(rank.columns)))
                    if not dates or not codes:
                        continue

                    mom = mom.loc[dates, codes]
                    rank = rank.loc[dates, codes]
                    w2 = w2.loc[dates]

                    # 1. momentum_score × rank
                    jongmok_score = mom * rank
                    # 2. 현금 비율 반영
                    jongmok_score = jongmok_score * (1 - self.현금비율)
                    # 3. 선정 종목(0 초과만 선정)
                    selected_df = jongmok_score.where(jongmok_score > 0, 0)
                    # 4. 날짜별 선정 종목 수
                    nonzero_counts = selected_df.apply(np.count_nonzero, axis=1)
                    # 5. 자산군 투자비중을 선정 종목에 균등 분배
                    jongmok_weight = selected_df.multiply(w2['value'] / nonzero_counts, axis=0).fillna(0)
                    weight_dict[asset] = jongmok_weight
                return weight_dict

            # 2) pandas 벡터화 방식 (최대한 for문 없이)
            def vectorized_weight_calc(momentum_dict, rank_dict, weight2_dict):
                weight_dict = {}
                for asset in keys_by_asset:
                    if asset == '현금':
                        continue
                    mom = momentum_dict.get(asset)
                    rank = rank_dict.get(asset)
                    w2 = weight2_dict.get(asset)
                    if mom is None or rank is None or w2 is None:
                        continue

                    dates = sorted(list(set(mom.index) & set(rank.index) & set(w2.index)))
                    codes = sorted(list(set(mom.columns) & set(rank.columns)))
                    if not dates or not codes:
                        continue

                    mom_ = mom.loc[dates, codes]
                    rank_ = rank.loc[dates, codes]
                    w2_ = w2.loc[dates]

                    jongmok_score = mom_ * rank_ * (1 - self.현금비율)
                    selected_df = jongmok_score.where(jongmok_score > 0, 0)
                    # 벡터화: 날짜별 종목 수 (broadcasting)
                    nonzero_counts = (selected_df > 0).sum(axis=1)
                    nonzero_counts = nonzero_counts.replace(0, np.nan)
                    jongmok_weight = selected_df.div(nonzero_counts, axis=0).multiply(w2_['value'], axis=0).fillna(0)
                    weight_dict[asset] = jongmok_weight
                return weight_dict

            # DB 읽기 → momentum_dict, rank_dict, weight2_dict 준비 (동일하게 두 방식 모두 사용)
            momentum_dict, rank_dict, weight2_dict = {}, {}, {}
            for asset, valid_dates in keys_by_asset.items():
                if not valid_dates:
                    continue
                marks = ','.join(['?'] * len(valid_dates))
                mom_df = pd.read_sql_query(
                    f"SELECT date, code, value FROM asset_info WHERE period = ? AND value_type = 'momentum_score' AND asset_type = ? AND date IN ({marks})",
                    conn, params=(period_str, asset, *valid_dates)
                )
                if not mom_df.empty:
                    mom_df['date'] = pd.to_datetime(mom_df['date'])
                    pivot_mom = mom_df.pivot(index='date', columns='code', values='value').sort_index()
                    momentum_dict[asset] = pivot_mom

                rank_df = pd.read_sql_query(
                    f"SELECT date, code, value FROM asset_info WHERE period = ? AND value_type = 'rank' AND asset_type = ? AND date IN ({marks})",
                    conn, params=(period_str, asset, *valid_dates)
                )
                if not rank_df.empty:
                    rank_df['date'] = pd.to_datetime(rank_df['date'])
                    pivot_rank = rank_df.pivot(index='date', columns='code', values='value').sort_index()
                    rank_dict[asset] = pivot_rank

                w2_df = pd.read_sql_query(
                    f"SELECT date, value FROM asset_info2 WHERE period = ? AND value_type = 'weight' AND asset_type = ? AND date IN ({marks})",
                    conn, params=(period_str, asset, *valid_dates)
                )
                if not w2_df.empty:
                    w2_df['date'] = pd.to_datetime(w2_df['date'])
                    w2_df = w2_df.set_index('date').sort_index()
                    weight2_dict[asset] = w2_df

            # 두 방식 계산
            # weight_dict_legacy = legacy_weight_calc(momentum_dict, rank_dict, weight2_dict)
            weight_dict_vec = vectorized_weight_calc(momentum_dict, rank_dict, weight2_dict)

            # 현금 비중 처리(두 방식 동일하게, for문 없이)
            현금_code = '114260'
            # if weight_dict_legacy:
            #     sample_asset = next(iter(weight_dict_legacy.values()))
            #     dates = sample_asset.index

            #     sum_df = sum([df.sum(axis=1) for k, df in weight_dict_legacy.items() if k != '현금'])
            #     현금_series = 1 - sum_df
            #     현금_df = pd.DataFrame(현금_series, columns=[현금_code])
            #     weight_dict_legacy['현금'] = 현금_df

            if weight_dict_vec:
                sample_asset = next(iter(weight_dict_vec.values()))
                dates = sample_asset.index

                sum_df = sum([df.sum(axis=1) for k, df in weight_dict_vec.items() if k != '현금'])
                현금_series = 1 - sum_df
                현금_df = pd.DataFrame(현금_series, columns=[현금_code])
                weight_dict_vec['현금'] = 현금_df

            if False:
                # 두 결과 비교

                def is_almost_equal(df1, df2):
                    # 인덱스, 컬럼 강제 정렬
                    df1 = df1.sort_index().sort_index(axis=1)
                    df2 = df2.sort_index().sort_index(axis=1)
                    # float형 강제 변환
                    df1 = df1.astype(float)
                    df2 = df2.astype(float)
                    # np.allclose로 값만 비교 (NaN은 0으로 대체)
                    return np.allclose(df1.fillna(0).values, df2.fillna(0).values)
                
                result_is_equal = True
                for asset in weight_dict_legacy.keys():
                    df1 = weight_dict_legacy[asset]
                    df2 = weight_dict_vec[asset]
                    if not is_almost_equal(df1, df2):
                        logging.warning(f"[{asset}] 레거시 방식과 벡터 연산 결과가 다릅니다. 차이나는 부분만 출력")
                        # 차이만 출력
                        diff = df1.compare(df2, keep_shape=True, keep_equal=False)
                        print("차이나는 부분만:")
                        print(diff)
                        input("엔터를 누르면 계속 진행합니다.")
                        result_is_equal = False
                    else:
                        logging.info(f"[{asset}] 레거시 방식과 벡터 연산 결과가 완전히 동일합니다.")
                        input("엔터를 누르면 계속 진행합니다.")


                if result_is_equal:
                    logging.info("레거시 방식과 벡터 연산 방식의 결과가 완전히 동일합니다.")
                    print("두 방식의 결과가 같습니다. 결과 예시(일부):")
                    for asset, df in weight_dict_legacy.items():
                        print(f"\n[{asset}] 일부 데이터:")
                        print(df.head())
                    input("결과를 확인하셨으면 엔터를 눌러주세요...")
                else:
                    print("!!! 두 방식의 결과가 다릅니다. 확인이 필요합니다.")

            if True:
                # 실제 저장 및 반환(한 방식 결과만 적용)
                total_inserted = 0
                for asset, df in weight_dict_vec.items():
                    for date, row in df.iterrows():
                        for code, value in row.items():
                            conn.execute(
                                "INSERT OR REPLACE INTO asset_info (date, asset_type, period, value_type, code, value) VALUES (?, ?, ?, 'weight', ?, ?)",
                                (date.strftime('%Y-%m-%d'), asset, period_str, code, float(value) if pd.notna(value) else None)
                            )
                            total_inserted += 1
                conn.commit()
                logging.info(f"    ----> 신규 weight {total_inserted}건 DB 저장 완료.")

            result_dict2 = {}
            if excel_save or return_full:
                if excel_save:
                    result_dict2 = self.get_all_weight_from_db(conn0=conn0, conn=conn, period_str=period_str)
                    if not excel_path:
                        excel_path = f"자산군별_종목당최종투자비중_dict_{self.period}.xlsx"
                    self.save_weight_dict_to_excel(result_dict2, excel_path)
                    logging.info(f"    ----> 엑셀 파일로 저장 완료: {excel_path}")
                if return_full:
                    if not excel_save:
                        result_dict2 = self.get_all_weight_from_db(conn0=conn0, conn=conn, period_str=period_str)
                    end_time = time.time()
                    logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                    return result_dict2
                else:
                    end_time = time.time()
                    logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                    return weight_dict_vec
            else:
                end_time = time.time()
                logging.info(f">>>>> 자산군별 현금혼합 절대평균모멘텀스코어 계산 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")
                return {}

    def get_all_weight_from_db(self, conn0, conn, period_str):
        """
        - 기준 날짜와 code는 asset_info의 value_type='close' 데이터 기준
        - value_type='weight' 값이 없는 경우 0으로 채운 DataFrame 반환
        - 반환: {asset_type: DataFrame(date x code)}
        """
        import pandas as pd

        asset_weight_dict = {}

        # 1. asset_type별 기준 date, code 구하기 (close 기준)
        close_df = pd.read_sql_query(
            "SELECT asset_type, date, code FROM asset_info WHERE period=? AND value_type='close'",
            conn0, params=(period_str,)
        )
        if close_df.empty:
            return asset_weight_dict

        for asset, subdf in close_df.groupby('asset_type'):
            dates = sorted(subdf['date'].unique())
            codes = sorted(subdf['code'].unique())

            # 2. 해당 asset_type의 weight값 가져오기
            weight_df = pd.read_sql_query(
                "SELECT date, code, value FROM asset_info WHERE period=? AND value_type='weight' AND asset_type=?",
                conn, params=(period_str, asset)
            )
            if not weight_df.empty:
                weight_df['date'] = pd.to_datetime(weight_df['date'])
                pivot_weight = weight_df.pivot(index='date', columns='code', values='value')
            else:
                # 데이터 없으면 빈 DataFrame 생성
                pivot_weight = pd.DataFrame(index=pd.to_datetime(dates), columns=codes)

            # 3. 인덱스, 컬럼을 기준으로 재정렬, 없는 값은 0
            pivot_weight = pivot_weight.reindex(
                index=pd.to_datetime(dates), columns=codes, fill_value=0
            ).sort_index()

            asset_weight_dict[asset] = pivot_weight

        return asset_weight_dict

    def get_latest_date_per_asset(self, conn, period_str, value_type):
        """
        asset_info에서 asset_type별 value_type의 최대 date 반환
        """
        q = """
            SELECT asset_type, MAX(date) as max_date
            FROM asset_info
            WHERE period=? AND value_type=?
            GROUP BY asset_type
        """
        df = pd.read_sql_query(q, conn, params=(period_str, value_type))
        return dict(zip(df['asset_type'], df['max_date']))

    def get_full_value_matrix(self, conn, period_str, value_type):
        """
        asset_info에서 value_type별 전체 (date x code) DataFrame dict 반환
        """
        q = """
            SELECT asset_type, date, code, value
            FROM asset_info
            WHERE period=? AND value_type=?
        """
        df = pd.read_sql_query(q, conn, params=(period_str, value_type))
        asset_dict = {}
        if df.empty:
            return asset_dict
        for asset, g in df.groupby('asset_type'):
            g['date'] = pd.to_datetime(g['date'])
            pivot = g.pivot(index='date', columns='code', values='value').sort_index()
            asset_dict[asset] = pivot
        return asset_dict

    def save_asset_dict_to_excel(self, asset_dict, path):
        with pd.ExcelWriter(path) as writer:
            for asset, df in asset_dict.items():
                # if asset == '현금':
                #     print(asset)
                #     print(df.tail(20))
                #     input(f"    ▶ {asset} 자산군의 데이터 확인 후 Enter...")
                df.to_excel(writer, sheet_name=str(asset)[:30])

    def calc_monthly_profit_rate(self, df_sell, df_buy, asset):
        # 월간수익률: sell / buy.shift(1) (날짜별로)
        df_profit = df_sell.divide(df_buy.shift(1))
        df_profit = df_profit.iloc[1:]  # 첫 행 NaN 제거
        # if asset == '현금':
        #     print(df_sell.tail(20))
        #     print(df_buy.tail(20))
        #     print(df_profit.tail(20))
        #     input("    ▶ 자산군별 월간수익률 계산 결과 확인 후 Enter...")
        return df_profit

    def 자산군별_월간수익률(self, sell, buy, excel_save=False, excel_path=None, return_full=True):
        """
        각 종목별로 월간수익률을 계산하고 DB(asset_info, value_type=profit_rate)에 저장, 필요시 엑셀로 저장합니다.
        """
        start_time = time.time()
        period_str = self.period_str
        logging.info(">>>>> 자산군별 월간 수익률 계산 시작[자산군별_월간수익률()]")

        conn = sqlite3.connect(self.db_price_daily_path)
        # 1. asset_type별 profit_rate, sell, buy 최신 date 확인
        last_profit = self.get_latest_date_per_asset(conn, period_str, 'profit_rate')
        last_sell = self.get_latest_date_per_asset(conn, period_str, sell)
        last_buy = self.get_latest_date_per_asset(conn, period_str, buy)

        # 2. asset_type별로 신규 계산이 필요한지 판단
        신규계산필요 = False
        신규계산_asset = []
        for asset in set(list(last_sell.keys()) + list(last_buy.keys())):
            last_pr = last_profit.get(asset, None)
            last_s = last_sell.get(asset, None)
            last_b = last_buy.get(asset, None)
            # 두 값이 모두 없는 경우 pass, sell/buy만 있음 → 계산 필요
            if (last_pr is None) or (max(last_s, last_b) > last_pr):
                신규계산필요 = True
                신규계산_asset.append(asset)
        logging.info(f"    -----> 신규 계산 필요: {신규계산필요}, 대상: {신규계산_asset}")

        # 3. 신규 계산 필요 없는 경우
        if not 신규계산필요:
            logging.info("    -----> 모든 자산군에서 추가 계산이 필요하지 않습니다.")
            if excel_save:
                result_dict = self.get_full_value_matrix(conn, period_str, 'profit_rate') if (excel_save or return_full) else {}
                if not excel_path:
                    excel_path = f"자산군별_월간수익률_dict_{self.period}.xlsx"
                self.save_asset_dict_to_excel(result_dict, excel_path)
                logging.info("    -----> 엑셀 파일에 저장하였습니다: %s", excel_path)
            if return_full:
                if not excel_save: 
                    result_dict = self.get_full_value_matrix(conn, period_str, 'profit_rate') if (excel_save or return_full) else {}
                    conn.close()
                    end_time = time.time()
                    logging.info(f">>>>> 자산군별 월간 수익률 계산 종료. 수행 시간: {end_time-start_time:.2f} 초\n")
                return result_dict 
            else: 
                end_time = time.time()
                logging.info(f">>>>> 자산군별 월간 수익률 계산 종료. 수행 시간: {end_time-start_time:.2f} 초\n")
                return {}

        # 4. 신규 계산 필요한 경우: 필요한 sell/buy 데이터만 읽고 계산
        logging.info("    -----> 일부 자산군에서 신규 월간수익률 계산 수행")
        result_dict = {}
        for asset in 신규계산_asset:
            last_pr = last_profit.get(asset, None) # profit_rate의 마지막 날짜



            buy_date = datetime.strptime(last_pr, '%Y-%m-%d').date()
            sell_date = last_sell # (buy_date + timedelta(days=1)).strftime('%Y%m%d')
            buy_date = buy_date.strftime('%Y%m%d')

            buy_date_cond = "AND date >= ?"
            sell_date_cond = "AND date > ?"
            params = [period_str, asset]
            if last_pr:
                params.append(last_pr)

            # sell
            df_sell = pd.read_sql_query(
                f"""
                SELECT date, code, value
                FROM asset_info
                WHERE period=? AND asset_type=? AND value_type='{sell}' {sell_date_cond}
                """, conn, params=params
            )
            # buy
            df_buy = pd.read_sql_query(
                f"""
                SELECT date, code, value
                FROM asset_info
                WHERE period=? AND asset_type=? AND value_type='{buy}' {buy_date_cond}
                """, conn, params=params
            )

            if df_sell.empty or df_buy.empty:
                continue

            df_sell['date'] = pd.to_datetime(df_sell['date'])
            df_buy['date'] = pd.to_datetime(df_buy['date'])
            sell_pivot = df_sell.pivot(index='date', columns='code', values='value').sort_index()
            buy_pivot = df_buy.pivot(index='date', columns='code', values='value').sort_index()
            profit_df = self.calc_monthly_profit_rate(sell_pivot, buy_pivot, asset)
            result_dict[asset] = profit_df

            # DB 저장 (asset_info에 INSERT OR REPLACE)
            with sqlite3.connect(self.db_path) as conn_w:
                for date, row in profit_df.iterrows():
                    for code, value in row.items():
                        conn_w.execute(
                            "INSERT OR REPLACE INTO asset_info (date, asset_type, period, value_type, code, value) VALUES (?, ?, ?, 'profit_rate', ?, ?)",
                            (date.strftime('%Y-%m-%d'), asset, period_str, code, float(value) if pd.notna(value) else None)
                        )
                conn_w.commit()
            logging.info(f"    ----->  {asset}: 신규 {len(profit_df)}개 date 계산 및 DB 저장")

        # 5. 최종 반환/엑셀 저장: excel_save/return_full 플래그 확인 후 처리
        if excel_save:
            final_dict = self.get_full_value_matrix(conn, period_str, 'profit_rate') if (excel_save or return_full) else {}
            if not excel_path:
                excel_path = f"자산군별_월간수익률_dict_{self.period}.xlsx"
            self.save_asset_dict_to_excel(final_dict, excel_path)
            logging.info("    -----> 엑셀 파일에 저장하였습니다: %s", excel_path)
        if return_full:
            if not excel_save: 
                final_dict = self.get_full_value_matrix(conn, period_str, 'profit_rate') if (excel_save or return_full) else {}
                conn.close()
                end_time = time.time()
                logging.info(f">>>>> 자산군별 월간 수익률 계산 종료. 수행 시간: {end_time-start_time:.2f} 초\n")
            return final_dict 
        else: 
            end_time = time.time()
            logging.info(f">>>>> 자산군별 월간 수익률 계산 종료. 수행 시간: {end_time-start_time:.2f} 초\n")
            return result_dict

    def get_data_from_db(
        self,
        period: str = 'daily',
        value_type: str = 'close',
        db_path: str = r'D:\_MPAA_Project\MPAA\MPAA_donna.db',
        table_name: str = 'asset_info'
    ) -> dict:
        """
        [MPAA] DB에서 자산군별 가격 데이터를 읽어 DataFrame 딕셔너리로 반환

        Args:
            period (str): 'daily', 'weekly', 'monthly' 등 데이터 주기
            price_type (str): 'close', 'open', 'avg' 등 가격 타입
            db_path (str): 데이터베이스 파일 경로 (기본값: 프로젝트 경로)
            table_name (str): 가격 데이터 테이블명 (기본값: 'price_data')

        Returns:
            dict: {asset_type: DataFrame(index=date, columns=code)}
                - 예: 전체자산_dict['국가'] → (date, 종목코드) DataFrame
                - 종가/시가/평균가 등 price_type에 따라 구분하여 반환

        Example:
            전체자산_dict = self.get_data_from_db(period='daily', price_type='close')
            전체자산_dict_open = self.get_data_from_db(period='daily', price_type='open')
            전체자산_dict_avg = self.get_data_from_db(period='daily', price_type='avg')
        """
        conn = sqlite3.connect(db_path)
        query = f"""
            SELECT date, asset_type, code, value
            FROM {table_name}
            WHERE period = ? AND value_type = ?
        """
        df = pd.read_sql_query(query, conn, params=(period, value_type))

        # <<<<<<<<<<<<<<<<<<<
        # 자산군(시트명) 목록을 동적으로 추출
        self.자산군 = list(df['asset_type'].unique())
        # >>>>>>>>>>>>>>>>>>>>>

        conn.close()

        asset_data_dict = {}
        for asset_type in df['asset_type'].unique():
            sub = df[df['asset_type'] == asset_type]
            pivoted = sub.pivot(index='date', columns='code', values='value')
            asset_data_dict[asset_type] = pivoted

        return asset_data_dict

    def 월간수익률(self, df):
        a = df / df.shift(1)
        return a

    def 평균모멘텀스코어(self, df, score_len, momentum_len):
        a = self.평균모멘텀(df=df, momentum_len=momentum_len)
        초기값 = 0
        for i in range(1, score_len+1):
            초기값 = np.where(df / df.shift(i) > 1, 1, 0) + 초기값
        a[a > -1] = 초기값/score_len
        return a

    def 평균모멘텀(self, df, momentum_len=12):
        초기값 = 0
        for i in range(1, momentum_len+1):
            초기값 = df / df.shift(i) + 초기값
        a = 초기값 / momentum_len
        return a

    def expand_cash_dataframe_index(self):
        """
        self.전체자산_dict는 weight_dict의 키(예: "국가", "섹터", "배당", "채권", "현금")와 동일한 키를 가지며,
        각 키는 m x n 형태의 DataFrame을 보유합니다.
        
        이 함수는 "현금"을 제외한 나머지 데이터프레임 중 인덱스 길이가 가장 긴 인덱스를 구한 후,
        "현금" 데이터프레임의 인덱스를 해당 인덱스로 확장합니다.
        
        확장된 부분(새로운 행)의 값은 기존 "현금" 데이터프레임의 첫번째 값(a[0])을 기준으로,
        역방향으로 다음과 같이 계산합니다:
            - a[-1] = a[0] * (self.현금비율 / 100)
            - a[-2] = a[-1] * (self.현금비율 / 100) = a[0] * (self.현금비율 / 100)^2
            - ...
            - a[-K] = a[0] * (self.현금비율 / 100)^K
        최종적으로 확장된 "현금" 데이터프레임을 self.전체자산_dict["현금"]에 저장합니다.
        """
        start_time = time.time()
        print(f"    >>>>> 현금 데이터 확장 시작[expand_cash_dataframe_index()]")
        union_index = None
        for key, df in self.전체자산_dict.items():
            if key != "현금":
                if union_index is None:
                    union_index = df.index
                else:
                    union_index = union_index.union(df.index)
        union_length = len(union_index)
        if union_index is None:
            print("            >>>>> 현금 외의 데이터프레임이 존재하지 않습니다.")
            return
        cash_df = self.전체자산_dict.get("현금")
        if cash_df is None:
            print("            >>>>> 현금 데이터가 존재하지 않습니다.")
            return
        current_length = len(cash_df.index)
        if current_length >= union_length:
            print("            >>>>> 현금 데이터프레임의 인덱스 길이가 이미 대상 인덱스와 같거나 큽니다.")
            return
        extended_cash = cash_df.reindex(union_index)
        new_indices = extended_cash[extended_cash.iloc[:, 0].isna()].index
        K = len(new_indices)
        if K == 0:
            print("            >>>>> 추가 확장할 인덱스가 없습니다.")
            return
        r = round(1 / (1 + self.현금비율 / 100.0), 4)
        r = 1 / (1 + self.현금비율 / 100.0)
        a0 = cash_df.iloc[0, 0]
        sorted_new_indices = list(new_indices)
        sorted_new_indices.sort()
        for i, idx in enumerate(sorted_new_indices):
            exponent = K - i
            extended_cash.loc[idx] = a0 * (r ** exponent)
        self.전체자산_dict["현금"] = extended_cash
        self.전체자산_dict_open["현금"] = extended_cash
        self.전체자산_dict_avg["현금"] = extended_cash
        print(f"            >>>>> '현금' 데이터프레임이 인덱스 길이 {current_length}에서 {union_length}로 확장되었습니다.")
        end_time = time.time()
        print(f"    >>>>> 현금 데이터 확장 종료. 함수 수행 시간: {end_time - start_time:.4f} 초\n")

if __name__ == "__main__":
    # 평균이동방법: 단순이동평균, 지수이동평균
    # loader = MPAA_strategy(mpaa_period="일", 평균이동방법="단순이동평균", 평균이동구간비율=30, 종목선정기준 = 1/3, 현금비율=0.25, b누적수익곡선적용=False, bGraphDisplay=True)
    loader = MPAA_strategy(mpaa_period="일", 평균이동방법="단순이동평균", 평균이동구간비율=30, 분봉시간='0910', 종목선정기준 = 1/3, 현금비율=0.25, b누적수익곡선적용=False, bGraphDisplay=True)

