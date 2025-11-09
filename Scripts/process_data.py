import argparse
import pandas as pd
import sqlite3
import os
#from validation import validate_no_negative_amount

def main(users_csv, orders_csv, output_db):
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_db), exist_ok=True)
    #os.makedirs(os.path.dirname(state_file), exist_ok=True)

    # Read CSVs
    users_df = pd.read_csv(users_csv)
    orders_df = pd.read_csv(orders_csv)


    # if validate_no_negative_amount(orders_df) is False:
    #     os.makedirs("validation.txt", exist_ok=True)
    #     #write validation failure log print the negative amounts
    #     with open("state/validation.txt", "w") as f:
    #         f.write("Data validation failed: Negative amounts found in orders.csv\n"+ orders_df[orders_df["amount"] < 0].to_string() )
        #print("Data validation failed. Exiting process.")
        #return
    
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
    
    

     #count number of columns in orders_df if more than 4 then find the column type and add alter statement to the table if not exists
    # if orders_df.shape[1]>4:
    #     for col in orders_df.columns[4:]:
    #         if col not in ['order_id','user_id','item_code','amount']:
    #             print(f"Additional column detected: {col}")
    #             col_type = 'TEXT'  # default type
    #             if pd.api.types.is_numeric_dtype(orders_df[col]):
    #                 col_type = 'REAL' if pd.api.types.is_float_dtype(orders_df[col]) else 'INTEGER'
    #             alter_query = f"ALTER TABLE user_orders ADD COLUMN {col} {col_type};"
    #             #update existing rows with null values for the new column to Mississauga if the column is place
    #             #if col=='place':
    #             Update_query = f"update user_orders set {col}='Mississauga';"
    #             conn.execute(Update_query)
    
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