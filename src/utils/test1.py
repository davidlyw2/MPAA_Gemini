import sqlite3
import pandas as pd

conn = sqlite3.connect("MPAA_Result.db")

# 1. 지표 데이터 샘플 확인
print("--- [daily_metrics] Sample ---")
print(pd.read_sql("SELECT * FROM daily_metrics LIMIT 3", conn))

# 2. 비중 데이터 샘플 확인 (가장 중요)
print("\n--- [daily_weights] Sample ---")
print(pd.read_sql("SELECT * FROM daily_weights LIMIT 10", conn))

# 3. 특정 날짜 데이터 존재 여부 테스트 (화면에 보였던 날짜 중 하나)
test_date = "2023-10-23" # 화면에서 클릭했던 날짜
print(f"\n--- Search Test for {test_date} ---")
res = pd.read_sql(f"SELECT * FROM daily_weights WHERE date LIKE '{test_date}%'", conn)
print(res)

conn.close()