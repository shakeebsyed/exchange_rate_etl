import os
import sqlite3
import pandas as pd

table_name = "exchange_rates"

def load_to_sqlite(df, db_path="exchange_rates.db"):
    print("Saving DB to:", os.path.abspath(db_path))
    conn = sqlite3.connect(db_path)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            d TEXT PRIMARY KEY,
            FXINRCAD REAL,
            FXUSDCAD REAL,
            FXSARCAD REAL,
            FXAUDCAD REAL,
            created_at TEXT DEFAULT (DATE('now'))
        )
    """)

    existing = pd.read_sql(f"select d from {table_name}", conn)
    existing_dates = set(existing['d'].tolist())

    new_rows = df[~df['d'].isin(existing_dates)]

    if new_rows.empty:
        print("No new Data to insert today.")
    else:
        new_rows.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"Added {len(new_rows)} new rows.")


    conn.close()
