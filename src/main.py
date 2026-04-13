import os
import sys

# 현재 파일(main.py)의 부모의 부모 폴더(MPAA_Gemini)를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) # 'D:\_MPAA_Project'까지 올라갈 경우
# 혹은 확실하게 'MPAA_Gemini' 폴더를 추가
sys.path.append(os.path.dirname(current_dir)) 

from src.config.invest_items import MPAA, weight_dict
import pandas as pd
import sqlite3
from src.config.invest_items import MPAA, weight_dict
from src.data.loader import init_result_db, get_last_calc_date, load_incremental_data
from src.engine.momentum import calculate_hit_ratio_score, allocate_weights, apply_meta_risk_manager
from src.engine.analytics import calculate_performance_metrics

def save_results_to_db_v1(metrics_df, final_weights, db_path="MPAA_Result.db"):
    """계산 결과를 Result DB에 저장"""
    conn = sqlite3.connect(db_path)
    
    try:
        # 1. 지표 저장
        # metrics_df에 'date' 컬럼이 인덱스로 있으므로 그대로 저장
        metrics_df.to_sql("daily_metrics", conn, 
                          if_exists='append', 
                          index=True, 
                          index_label='date', 
                          chunksize=1000) # 변수 제한 방지
        
        # 2. 비중 저장 (Wide -> Long 변환)
        weights_long = final_weights.stack().reset_index()
        weights_long.columns = ['date', 'code', 'weight']
        
        # 비중이 0인 데이터는 저장하지 않음 (DB 용량 최적화)
        weights_long = weights_long[weights_long['weight'] > 0]
        
        # 비중 데이터 저장
        weights_long.to_sql("daily_weights", conn, 
                            if_exists='append', 
                            index=False, 
                            chunksize=1000, # 변수 제한 방지
                            method='multi') # 속도 향상을 위해 유지하되 chunksize로 제한
        
        print(f"✅ DB 저장 완료: {len(metrics_df)}행 추가됨.")
        
    except Exception as e:
        print(f"❌ DB 저장 중 오류 발생: {e}")
    finally:
        conn.close()


def save_results_to_db(metrics_df, final_weights, db_path="MPAA_Result.db"):
    """계산 결과를 Result DB에 저장"""
    conn = sqlite3.connect(db_path)
    
    try:
        # 1. 지표 저장
        metrics_df.to_sql("daily_metrics", conn, if_exists='append', index=True, index_label='date', chunksize=1000)
        
        # 2. 비중 저장 전 데이터 확인 (디버깅용)
        print(f"DEBUG: final_weights shape = {final_weights.shape}")
        
        # Wide -> Long 변환
        weights_long = final_weights.stack().reset_index()
        weights_long.columns = ['date', 'code', 'weight']
        
        # 날짜 포맷 통일 (00:00:00 제거 및 문자열화)
        weights_long['date'] = pd.to_datetime(weights_long['date']).dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # 비중이 아주 미세하게라도 있는 것들만 추출 (필터링 조건 완화)
        weights_long = weights_long[weights_long['weight'] > 0.0001]
        
        print(f"DEBUG: 저장할 비중 데이터 개수 = {len(weights_long)}")

        if len(weights_long) > 0:
            weights_long.to_sql("daily_weights", conn, if_exists='append', index=False, chunksize=1000, method='multi')
            print(f"✅ 비중 데이터 {len(weights_long)}건 저장 완료.")
        else:
            print("⚠️ 경고: 저장할 비중 데이터가 없습니다. (모든 비중이 0임)")
        
    except Exception as e:
        print(f"❌ DB 저장 중 오류 발생: {e}")
    finally:
        conn.close()

def run_incremental_update():
    PRICE_DB = "MPAA_price.db"
    RESULT_DB = "MPAA_Result.db"
    
    init_result_db(RESULT_DB)
    last_date = get_last_calc_date(RESULT_DB)
    
    # 티커 리스트 준비
    all_tickers = list(set([t for cat in MPAA.values() for t in cat.keys()] + ["114260"]))
    
    print(f"🔄 마지막 계산 날짜: {last_date or '없음 (전체 계산 시작)'}")
    prices = load_incremental_data(PRICE_DB, all_tickers, last_date)
    
    # 신규 데이터 유무 확인
    if last_date and prices.index[-1].strftime('%Y-%m-%d') <= last_date:
        print("✅ 최신 상태입니다. 추가 계산이 필요하지 않습니다.")
        return

    # 신규 데이터만 필터링하여 계산 (스코어는 전체 기간 필요)
    scores = calculate_hit_ratio_score(prices)
    core_weights = allocate_weights(scores, MPAA, weight_dict)
    final_weights, _ = apply_meta_risk_manager(core_weights, prices)
    metrics_dict, cum_returns, drawdown = calculate_performance_metrics(final_weights, prices)
    
    # DataFrame 정리
    metrics_df = pd.DataFrame({
        "total_return": (cum_returns - 1),
        "drawdown": drawdown,
        "cum_return": cum_returns
        # CAGR, Sharpe는 전체 기간 지표이므로 일별 저장 시 필요한 경우 추가 연산
    }, index=prices.index)

    # 신규 데이터 구간만 추출
    if last_date:
        new_mask = metrics_df.index > pd.to_datetime(last_date)
        metrics_df = metrics_df[new_mask]
        final_weights = final_weights[new_mask]

    if not metrics_df.empty:
        save_results_to_db(metrics_df, final_weights, RESULT_DB)
        print(f"🚀 {len(metrics_df)}일치 신규 데이터 업데이트 완료!")
    else:
        print("데이터가 충분하지 않습니다.")

if __name__ == "__main__":
    run_incremental_update()