import sqlite3
import pandas as pd
import os

def load_from_db(db_path, tickers):
    """
    asset_info 테이블에서 요청한 ticker들의 종가(close) 데이터를 가져와 Wide Format으로 반환
    """
    conn = sqlite3.connect(db_path)
    
    # 1. 쿼리문: value_type이 close인 데이터만 추출
    ticker_list = "', '".join(tickers)
    query = f"""
    SELECT date, code, value as close
    FROM asset_info
    WHERE code IN ('{ticker_list}') 
      AND value_type = 'close'
    """
    
    df_raw = pd.read_sql(query, conn)
    conn.close()
    
    # 2. 전처리: 중복 제거 및 Wide Format 변환
    # 데이터에 동일 날짜/종목 중복이 있을 수 있으므로 drop_duplicates 적용
    df_raw = df_raw.drop_duplicates(['date', 'code'])
    price_df = df_raw.pivot(index='date', columns='code', values='close')
    
    # 3. 인덱스 타입 변환 및 정렬
    price_df.index = pd.to_datetime(price_df.index)
    price_df = price_df.sort_index()
    
    return price_df