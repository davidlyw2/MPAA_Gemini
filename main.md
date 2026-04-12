# 📄 MPAA V3.1 Hybrid Simulator Blueprint

## 1. System Overview
본 시스템은 **승률(Hit-Ratio) 기반의 이중 모멘텀 엔진**과 **수익곡선 추적형 메타 리스크 매니저**를 결합한 하이브리드 자산배분 시뮬레이터입니다. 모든 연산은 `Pandas` 및 `NumPy`를 활용하여 벡터화되었으며, SQLite DB(`MPAA_price.db`)와의 유기적 연동을 통해 실전과 유사한 백테스트 환경을 제공합니다.

---

## 2. Data Architecture & Preprocessing
* **Source:** `MPAA_price.db` 내 `asset_info` 테이블 (Long Format).
* **Filtering:** `value_type = 'close'`(종가) 데이터만 추출하며, `invest_items.py`의 티커 리스트를 기준으로 Wide Format으로 변환합니다.
* **Dynamic Scaling:** 신규 상장 종목(상장 후 63일 이상)은 가용 데이터 일수 $N$만큼 동적으로 스케일링하여 평가하며, 63일 미만은 계산에서 제외합니다.
* **Time Isolation:** 모든 결정은 $T-1$ 시점까지의 데이터만 참조하여 미래 데이터를 미리 보는 오류(Look-ahead Bias)를 방지합니다.

---

## 3. Core Momentum Engine (V3.1)
* **Scoring Logic (Hit-Ratio):** 과거 $d$일(1~252일) 전 가격과 현재가를 비교하여 $P_t \ge P_{t-d}$인 비율을 0~1 사이 스코어로 산출합니다.
* **Relative Momentum:** 각 카테고리(국가, 섹터, 배당, 채권)별로 스코어 상위 30% 종목을 추출합니다. (카테고리당 최소 1종목 보장)
* **Absolute Momentum:** 선정된 종목의 최종 비중은 `(카테고리 할당 비중 / 선정 종목 수) * Individual Score`로 결정합니다.
* **Cash Switching:** 모멘텀이 부족하여 할당되지 못한 모든 잉여 비중은 **현금(114260 KODEX 국고채3년)**으로 자동 전환합니다.

---

## 4. Meta Risk Manager (Equity Guard)
* **Equity Curve Tracking:** 코어 엔진의 결과를 바탕으로 $T-1$ 시점까지의 가상 계좌 누적 수익 곡선을 실시간 생성합니다.
* **Meta Scoring:** 수익곡선 자체를 다시 한번 Hit-Ratio 로직(관측 126일)으로 평가하여 0~1 사이의 $Score_{meta}$를 산출합니다.
* **Double Rebalancing:** 최종 비중은 `Core Weight * Meta Score`로 삭감 조정하며, 삭감된 모든 비중은 다시 현금(114260)으로 글로벌 스위칭하여 하락장 방어력을 극대화합니다.

---

## 5. Performance Analytics
* **Key Metrics:** CAGR(연평균 성장률), MDD(최대 낙폭), Sharpe Ratio(위험 대비 수익률), 전체 누적 수익률을 산출합니다.
* **Visual Analysis:** 전체 백테스트 기간의 수익곡선(Equity Curve)과 낙폭(Drawdown) 시계열 데이터를 생성하여 전략의 견고함을 검증합니다.

---

## 6. Project File Structure
```text
MPAA_Gemini/
├── src/
│   ├── config/
│   │   └── invest_items.py      # ETF 목록 및 자산군별 비중 설정
│   ├── data/
│   │   └── loader.py            # SQLite DB 연동 및 데이터 전처리
│   ├── engine/
│   │   ├── momentum.py          # 스코어링, 비중 할당, 메타 엔진 로직
│   │   └── analytics.py         # 성과 지표 분석 모듈
│   └── main.py                  # 전체 프로세스 통합 실행 및 리포트 출력
└── MPAA_price.db                # 시세 데이터베이스