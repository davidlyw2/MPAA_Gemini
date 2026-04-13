import sqlite3
import pandas as pd
import os

def init_result_db(db_path="MPAA_Result.db"):
    """결과 저장을 위한 DB 및 테이블 초기화"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # 일별 지표 테이블
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_metrics (
            date TEXT PRIMARY KEY,
            total_return REAL, cagr REAL, mdd REAL, sharpe REAL, drawdown REAL, cum_return REAL
        )
    """)
    # 일별 비중 테이블 (비중 > 0 종목만)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_weights (
            date TEXT, code TEXT, weight REAL,
            PRIMARY KEY (date, code)
        )
    """)
    conn.commit()
    conn.close()

def get_last_calc_date(db_path="MPAA_Result.db"):
    """결과 DB의 마지막 날짜 확인"""
    if not os.path.exists(db_path): return None
    try:
        conn = sqlite3.connect(db_path)
        res = pd.read_sql("SELECT MAX(date) as last_date FROM daily_metrics", conn)
        conn.close()
        return res.iloc[0]['last_date']
    except: return None

def load_incremental_data(price_db_path, tickers, last_date=None):
    """신규 계산에 필요한 데이터만 로드 (마지막 날짜 기준 252일 전부터)"""
    conn = sqlite3.connect(price_db_path)
    ticker_list = "', '".join(tickers)
    
    query = f"SELECT date, code, value as close FROM asset_info WHERE code IN ('{ticker_list}') AND value_type = 'close'"
    if last_date:
        # 스코어 계산을 위해 마지막 날짜 기준 약 1년 전 데이터부터 가져옴
        query += f" AND date >= date('{last_date}', '-380 days')"
    
    df_raw = pd.read_sql(query, conn)
    conn.close()
    
    df_raw = df_raw.drop_duplicates(['date', 'code'])
    price_df = df_raw.pivot(index='date', columns='code', values='close')
    price_df.index = pd.to_datetime(price_df.index)
    return price_df.sort_index()