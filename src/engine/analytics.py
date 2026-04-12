import pandas as pd
import numpy as np

def calculate_performance_metrics(final_weights, price_df):
    """
    최종 비중과 가격 데이터를 바탕으로 백테스트 성과 지표를 계산합니다.
    """
    # 1. 일별 수익률 계산 (T-1 비중 * T일 수익률)
    asset_returns = price_df.pct_change().fillna(0)
    port_returns = (final_weights * asset_returns).sum(axis=1)
    
    # 2. 누적 수익률 (Equity Curve)
    cum_returns = (1 + port_returns).cumprod()
    
    # 3. MDD (Maximum Drawdown)
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    max_drawdown = drawdown.min()
    
    # 4. CAGR (연평균 성장률)
    n_years = len(port_returns) / 252
    total_return = cum_returns.iloc[-1]
    cagr = (total_return ** (1 / n_years)) - 1 if n_years > 0 else 0
    
    # 5. Sharpe Ratio (무위험 수익률 0% 가정)
    daily_std = port_returns.std()
    sharpe_ratio = (port_returns.mean() / daily_std) * np.sqrt(252) if daily_std != 0 else 0
    
    metrics = {
        "Total Return": f"{(total_return - 1) * 100:.2f}%",
        "CAGR": f"{cagr * 100:.2f}%",
        "MDD": f"{max_drawdown * 100:.2f}%",
        "Sharpe Ratio": f"{sharpe_ratio:.2f}",
        "Current Drawdown": f"{drawdown.iloc[-1] * 100:.2f}%"
    }
    
    return metrics, cum_returns, drawdown

    