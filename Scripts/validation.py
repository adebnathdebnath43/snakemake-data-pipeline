# scripts/validation.py
import pandas as pd
import sys
import os

def validate_no_negative_amount(orders_df):
    if (orders_df["amount"] < 0).any():
        print("FAILED: Negative amount found in orders.csv", orders_df[orders_df["amount"] < 0])
        return False
    print("PASSED: No negative amounts")
    return True

def validate_no_missing_order_id(orders_df):
    if orders_df["order_id"].isna().any():
        print("FAILED: Missing order_id in orders.csv")
        return False
    if not pd.to_numeric(orders_df["order_id"], errors='coerce').notna().all():
        print("FAILED: Non-numeric order_id")
        return False
    print("PASSED: All order_id valid")
    return True

def validate_user_ids_exist(users_df, orders_df):
    missing = set(orders_df["user_id"]) - set(users_df["user_id"])
    if missing:
        print(f"FAILED: user_id not in users.csv: {sorted(missing)}")
        return False
    print("PASSED: All user_id exist")
    return True

def main(users_csv, orders_csv, state_folder="state"):
    os.makedirs(state_folder, exist_ok=True)

    users_df = pd.read_csv(users_csv)
    orders_df = pd.read_csv(orders_csv)

    results = [
        validate_no_negative_amount(orders_df),
        validate_no_missing_order_id(orders_df),
        validate_user_ids_exist(users_df, orders_df)
    ]

    all_passed = all(results)

    with open(os.path.join(state_folder, "validation_results.txt"), "w") as f:
        f.write("All checks PASSED\n" if all_passed else "Some checks FAILED\n")

    if not all_passed:
        sys.exit(1)
    else:
        print("All validation passed. Proceeding...")

#if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: validation.py <users.csv> <orders.csv>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])