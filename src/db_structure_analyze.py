import sqlite3
import pandas as pd
import os

# 1. 실행 파일의 위치를 기준으로 DB 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__)) # src 폴더
project_root = os.path.dirname(current_dir)             # MPAA_Gemini 폴더
#db_path = os.path.join(project_root, "MPAA_price.db")
#db_path = os.path.join(project_root, "MPAA_data_단순이동평균_30.db")
db_path = os.path.join(project_root, "MPAA_price_min.db")

def inspect_db(path):
    print(f"🔍 시도 중인 DB 경로: {path}")
    if not os.path.exists(path):
        print(f"❌ 파일을 찾을 수 없습니다. 현재 폴더 목록: {os.listdir(project_root)}")
        return

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # 1. 테이블 목록 조회
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"📂 [테이블 목록]: {tables}")

    for table_info in tables:
        table_name = table_info[0]
        print(f"\n--- 📊 Table: {table_name} ---")
        
        # 2. 컬럼 정보 조회
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()
        print("  [컬럼 정보] (id, name, type, ...)")
        for col in columns:
            print(f"   - {col[1]} ({col[2]})")

        # 3. 데이터 샘플 조회
        try:
            df_sample = pd.read_sql(f"SELECT * FROM '{table_name}' LIMIT 5;", conn)
            print("\n  [데이터 샘플 (Top 5)]")
            print(df_sample)
        except Exception as e:
            print(f"  ⚠️ 샘플 로드 실패: {e}")

    conn.close()

if __name__ == "__main__":
    inspect_db(db_path)