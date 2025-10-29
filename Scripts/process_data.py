import argparse
import pandas as pd
import sqlite3
import os

def main(users_csv, orders_csv, output_db):
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_db), exist_ok=True)
    
    # Read CSVs
    users_df = pd.read_csv(users_csv)
    orders_df = pd.read_csv(orders_csv)
    
    # Inner join on user_id
    merged_df = pd.merge(users_df, orders_df, on='user_id', how='inner')
    
    # Write to SQLite table 'user_orders'
    conn = sqlite3.connect(output_db)
    merged_df.to_sql('user_orders', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"Success! Merged {len(merged_df)} rows into {output_db}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSVs and load to SQLite")
    parser.add_argument('--users_csv', required=True, help="Path to users.csv")
    parser.add_argument('--orders_csv', required=True, help="Path to orders.csv")
    parser.add_argument('--output_db', required=True, help="Path to output SQLite DB")
    args = parser.parse_args()
    main(args.users_csv, args.orders_csv, args.output_db)