import os
import sys

# 상위 폴더들을 경로에 추가하여 모듈 임포트 가능하게 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from src.config.invest_items import MPAA, weight_dict
from src.data.loader import load_from_db
from src.engine.momentum import calculate_hit_ratio_score, allocate_weights, apply_meta_risk_manager
from src.engine.analytics import calculate_performance_metrics

# 1. 경로 설정
db_path = os.path.join(os.path.dirname(current_dir), "MPAA_price.db")

# 2. 전체 티커 리스트 추출 (현금 종목 114260 포함)
all_tickers = []
for cat in MPAA.values():
    all_tickers.extend(list(cat.keys()))
all_tickers = list(set(all_tickers + ["114260"]))

def run_simulation_v0():
    print("⏳ 데이터 로딩 중...")
    prices = load_from_db(db_path, all_tickers)
    
    print("⏳ 모멘텀 스코어 계산 중 (이 작업은 다소 시간이 소요될 수 있습니다)...")
    scores = calculate_hit_ratio_score(prices)
    
    print("⏳ 최종 비중 계산 중...")
    weights = allocate_weights(scores, MPAA, weight_dict)
    
    # 결과 확인
    print("\n✅ 최근 5거래일 최종 투자 비중:")
    print(weights.tail().round(4))
    
    # CSV 저장 (선택 사항)
    # weights.to_csv("mpaa_final_weights.csv")
    return weights

def run_simulation_v1():
    print("⏳ [1/4] 데이터 로딩 중...")
    prices = load_from_db(db_path, all_tickers)
    
    print("⏳ [2/4] 코어 모멘텀 계산 중...")
    scores = calculate_hit_ratio_score(prices)
    
    print("⏳ [3/4] 1차 비중 배분 중...")
    core_weights = allocate_weights(scores, MPAA, weight_dict)
    
    print("⏳ [4/4] 메타 방어 엔진 가동 및 최종 비중 산출...")
    final_weights, equity_curve = apply_meta_risk_manager(core_weights, prices)
    
    # --- 결과 출력 ---
    print("\n" + "="*50)
    print("🏆 MPAA V3.1 시뮬레이션 완료")
    print("="*50)
    print(f"최종 분석 일자: {final_weights.index[-1].date()}")
    
    print("\n[최종 포트폴리오 구성]")
    top_assets = final_weights.iloc[-1].sort_values(ascending=False)
    print(top_assets[top_assets > 0.01].round(4)) # 비중 1% 이상만 출력
    
    print("\n[방어 신호]")
    # 메타 엔진의 마지막 스코어 확인 (1.0에 가까울수록 공격적, 0에 가까울수록 방어적)
    last_equity_return = (equity_curve.iloc[-1] / equity_curve.iloc[-2] - 1).values[0]
    print(f"현재 계좌 추세(Meta Score): {final_weights.sum(axis=1).iloc[-1]:.2f} (1.0이 최고)")
    
    return final_weights

def run_simulation():
    print("⏳ [1/5] 데이터 로딩 및 전처리...")
    prices = load_from_db(db_path, all_tickers)
    
    print("⏳ [2/5] 코어 모멘텀 계산 (Hit-Ratio)...")
    scores = calculate_hit_ratio_score(prices)
    
    print("⏳ [3/5] 1차 자산 배분 (Relative & Absolute)...")
    core_weights = allocate_weights(scores, MPAA, weight_dict)
    
    print("⏳ [4/5] 메타 리스크 매니저 가동 (Equity Curve Guard)...")
    final_weights, _ = apply_meta_risk_manager(core_weights, prices)
    
    print("⏳ [5/5] 성과 지표 분석 중...")
    metrics, cum_returns, drawdown = calculate_performance_metrics(final_weights, prices)
    
    # --- 최종 리포트 출력 ---
    print("\n" + "="*50)
    print("📊 MPAA V3.1 BACKTEST REPORT")
    print("="*50)
    for k, v in metrics.items():
        print(f"{k:<20} : {v}")
    
    print("\n[현재 TOP 5 포트폴리오 비중]")
    last_weights = final_weights.iloc[-1].sort_values(ascending=False).head(5)
    print(last_weights.round(4))
    
    print("\n" + "="*50)
    print("✅ 시뮬레이션이 성공적으로 완료되었습니다.")
    
    # CSV로 결과 저장 (필요 시)
    # final_weights.to_csv("final_weights.csv")
    
    return final_weights, metrics


if __name__ == "__main__":
    run_simulation()