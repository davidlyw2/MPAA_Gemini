import pandas as pd
import numpy as np

def calculate_hit_ratio_score(price_df: pd.DataFrame, min_periods: int = 63, max_lookback: int = 252):
    """
    승률 기반 모멘텀 스코어(Hit-Ratio)를 벡터화 연산으로 계산합니다.
    
    Logic:
    - 1일부터 max_lookback일까지 각 d일 전 가격과 현재 가격을 비교.
    - 현재가 >= d일전 가격 이면 1점, 아니면 0점.
    - 가용 가능한 모든 d에 대한 점수의 평균을 산출 (0~1).
    """
    
    # 1. 결측치 처리 (거래 정지 등 대응)
    price_df = price_df.ffill()
    
    # 2. 각 d일 전 가격과의 비교 결과를 담을 3D-like 구조 (또는 합산용 컨테이너)
    # 메모리 효율을 위해 합계(score_sum)와 가운트(valid_count)를 관리합니다.
    score_sum = pd.DataFrame(0.0, index=price_df.index, columns=price_df.columns)
    valid_count = pd.DataFrame(0.0, index=price_df.index, columns=price_df.columns)
    
    # 3. 1일부터 max_lookback까지 순회 (이 루프는 설정값 순회이므로 시계열 for문이 아님)
    for d in range(1, max_lookback + 1):
        # d일 전 가격 가져오기
        shifted_price = price_df.shift(d)
        
        # 유효한 비교군 마스크 (상장 초기 제외)
        mask = shifted_price.notna()
        
        # 이진 스위치 판정: 현재가 >= d일전 가격 (True=1, False=0)
        # np.where를 사용하여 벡터화 판정
        win = np.where(price_df >= shifted_price, 1.0, 0.0)
        
        # 마스크를 적용하여 유효한 데이터만 합산
        score_sum += np.where(mask, win, 0.0)
        valid_count += mask.astype(float)
    
    # 4. 최종 스코어 계산 (Score = 점수 합계 / 유효 비교 횟수)
    hit_ratio_score = score_sum / valid_count
    
    # 5. 신규 상장 종목 필터링 (63거래일 미만은 NaN 처리 후 drop 방안 마련)
    # cumulative count를 사용하여 상장 후 경과 일수를 체크합니다.
    listing_days = price_df.notna().cumsum()
    hit_ratio_score = hit_ratio_score.where(listing_days >= min_periods, np.nan)
    
    return hit_ratio_score

# [참고] 위 함수는 전체 시계열을 통째로 계산하므로 T-1 시점 데이터 격리는 
# 호출부에서 .loc[:T-1] 혹은 .shift(1)된 데이터를 입력함으로써 보장됩니다.

def allocate_weights(score_df, mpaa_config, weight_dict):
    """
    각 시점(T)별로 카테고리 내 상위 종목을 선정하고 최종 비중을 계산합니다.
    """
    final_weights = pd.DataFrame(0.0, index=score_df.index, columns=score_df.columns)
    cash_ticker = "114260" # KODEX 국고채3년
    
    total_group_weight = sum(weight_dict.values())
    
    for category, tickers in mpaa_config.items():
        if category == "현금": continue
        
        # 1. 해당 카테고리 종목들의 스코어만 추출
        cat_tickers = list(tickers.keys())
        cat_scores = score_df[cat_tickers]
        
        # 2. T-1 시점 스코어를 기준으로 순위 계산 (Vectorized Rank)
        # 상위 30% 개수 산출
        n_top = max(1, round(len(cat_tickers) * 0.3))
        
        # 행별(날짜별) 랭킹 산출 (스코어 높은 것이 1등)
        ranks = cat_scores.rank(axis=1, ascending=False)
        
        # 3. 상위 30% 마스크 생성
        top_mask = ranks <= n_top
        
        # 4. 개별 종목 비중 계산
        # (카테고리 비중 / 선정 종목 수) * 스코어
        group_share = weight_dict[category] / total_group_weight
        base_weight_per_stock = group_share / n_top
        
        # 선정된 종목의 비중: 스코어만큼 투자
        target_etf_weights = cat_scores[top_mask] * base_weight_per_stock
        final_weights[cat_tickers] = target_etf_weights.fillna(0.0)
        
        # 5. 나머지(1-Score)는 현금으로 스위칭
        # 카테고리에 할당된 총 비중에서 실제 ETF에 할당된 비중의 합을 뺌
        assigned_sum = target_etf_weights.sum(axis=1)
        remaining_cash = group_share - assigned_sum
        final_weights[cash_ticker] += remaining_cash
        
    return final_weights

def apply_meta_risk_manager(weights_df, price_df, cash_ticker="114260"):
    """
    수익곡선 모멘텀을 계산하여 최종 비중을 삭감하고 현금으로 스위칭합니다.
    """
    # 1. 일별 수익률 계산
    returns_df = price_df.pct_change().fillna(0)
    
    # 2. 포트폴리오 일별 수익률 (T일 비중 * T일 수익률)
    # weights_df는 이미 shift(1) 처리가 되어 있으므로 당일 수익률과 바로 곱함
    port_returns = (weights_df * returns_df).sum(axis=1)
    
    # 3. 가상 누적 수익곡선 (Equity Curve)
    equity_curve = (1 + port_returns).cumprod().to_frame(name='equity')
    
    # 4. 수익곡선에 대한 승률 스코어 계산 (메타 스코어)
    # 관측 기간을 126일(약 6개월)로 설정하여 중기 추세 반영
    meta_score_df = calculate_hit_ratio_score(equity_curve, min_periods=20, max_lookback=126)
    meta_score = meta_score_df['equity']
    
    # 5. 비중 조절: (기존 비중 * 메타 스코어)
    # meta_score가 0.5라면 모든 위험자산 비중을 절반으로 줄임
    final_weights = weights_df.mul(meta_score, axis=0).fillna(0)
    
    # 6. 줄어든 만큼 현금(국고채3년)으로 스위칭
    total_assigned = final_weights.sum(axis=1)
    final_weights[cash_ticker] += (1.0 - total_assigned)
    
    return final_weights, equity_curve
    
        