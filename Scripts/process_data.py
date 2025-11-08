import argparse
import pandas as pd
import sqlite3
import os

def main(users_csv, orders_csv, output_db):
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_db), exist_ok=True)
    #os.makedirs(os.path.dirname(state_file), exist_ok=True)

    # Read CSVs
    users_df = pd.read_csv(users_csv)
    orders_df = pd.read_csv(orders_csv)
    # make the last order as 0 from non existing state file
    # last_order_id = 0
    # if os.path.exists(state_file):
    #     with open(state_file, 'r') as f:
    #         last_order_id = int(f.read().strip()) 
    
    # Inner join on user_id
    merged_df = pd.merge(users_df, orders_df, on='user_id', how='inner')

    #filter new orders only
    #merged_df=merged_df[merged_df['order_id']>last_order_id].copy()
    #merge date to new rows
    merged_df['merge_date']=pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write to SQLite table 'user_orders'
    conn = sqlite3.connect(output_db)
    merged_df.to_sql('user_orders', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()
   
    # Update state file with the last processed order_id
    # last_order_id = merged_df['order_id'].max()
    # with open(state_file, 'w') as f:
    #     f.write(str(last_order_id))   

    conn.close()
    
    print(f"Success! Merged {len(merged_df)} rows into {output_db}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSVs and load to SQLite")
    parser.add_argument('--users_csv', required=True, help="Path to users.csv")
    parser.add_argument('--orders_csv', required=True, help="Path to orders.csv")
    parser.add_argument('--output_db', required=True, help="Path to output SQLite DB")
    #parser.add_argument('--state_file', required=True, help="Path to state file")
    args = parser.parse_args()
    main(args.users_csv, args.orders_csv, args.output_db)