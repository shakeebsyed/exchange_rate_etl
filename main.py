from extract.fetch_data import fetch_exchange_data
from transform.clean_data import clean_exchange_data
from load.load_to_db import load_to_sqlite

if __name__ == "__main__":
    print("Fetching data...")
    df = fetch_exchange_data()

    print("Cleaning data...")
    df = clean_exchange_data(df)

    print("Loading data to SQLite...")
    load_to_sqlite(df)

    print("ETL process complete!")
