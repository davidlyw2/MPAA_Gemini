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

## 6. Data Continuity & Update Logic
* **Incremental Processing:** 매번 전체 기간을 재계산하는 대신, `MPAA_Result.db`의 마지막 기록 날짜를 확인하여 신규 데이터만 연산하는 증분 업데이트 방식을 채택합니다.
* **SQLite Double-Buffering:** 원천 데이터(`MPAA_price.db`)와 결과 데이터(`MPAA_Result.db`)를 분리하여 데이터 무결성을 유지하고 처리 속도를 최적화합니다.
* **Storage Optimization:** 비중 데이터 저장 시 값이 0인 항목은 제외하고, `chunksize` 파라미터를 조정하여 SQLite의 SQL 변수 제한(999개) 에러를 방지합니다.

---

## 7. Visualization & Monitoring (Dash)
* **Hybrid Dashboard:** `Plotly Dash`를 활용하여 웹 기반 분석 환경을 제공합니다.
* **Dual-Pane Charts:** 상단에는 누적 수익률 곡선을, 하단에는 MDD와 Sharpe Ratio를 배치하여 수익과 리스크를 동시에 모니터링합니다.
* **Interactive Weight Lookup:** 차트의 특정 시점(날짜)을 클릭하면 해당 날짜의 상세 ETF 포트폴리오 비중을 하단 테이블에 실시간으로 출력합니다.
* **Responsive Layout:** 브라우저 창 크기에 따라 그래프 크기가 유동적으로 조절되는 가변형 레이아웃을 적용했습니다.

---

## 8. Operations & Security (Git Workflow)
* **Automated Guard (g-all):** PowerShell 기반의 커스텀 함수를 통해 업로드 전 보안 검사를 자동화합니다.
* **Data Exclusion:** `.gitignore` 및 사전 스캔 로직을 통해 대용량 DB 파일(`.db`)과 기술 문서(`.pdf`, `.xlsx`, `.pptx`, `.md`)가 Public Repository에 유출되는 것을 원천 차단합니다.
* **Encoding Optimization:** 터미널 및 파일 인코딩을 UTF-8로 강제 설정하여 윈도우 환경에서의 한글 깨짐 및 Git 인덱싱 오류를 해결했습니다.

---

## 9. Expanded Project File Structure
```text
MPAA_Gemini/
├── src/
│   ├── config/
│   │   ├── invest_items.py      # ETF 목록 및 비중 설정
│   │   └── menulist.py          # (신규) 시스템 메뉴 및 UI 설정
│   ├── data/
│   │   └── loader.py            # SQLite DB 로더
│   ├── engine/
│   │   ├── momentum.py          # 핵심 모멘텀 및 메타 엔진
│   │   └── analytics.py         # 성과 지표 산출
│   ├── dashboard/
│   │   └── app.py               # (신규) Dash 웹 대시보드 메인
│   └── main.py                  # 전체 프로세스 통합 및 증분 업데이트 실행
├── MPA_price.db                 # 원천 시세 데이터베이스
├── MPAA_Result.db               # (신규) 백테스트 결과 및 비중 저장 DB
└── .gitignore