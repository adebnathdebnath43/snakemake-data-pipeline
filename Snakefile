rule all:
    input:
        "data/processed/analytics.sqlite"

rule process_data:
    input:
        users="data/raw/users.csv",
        orders="data/raw/orders.csv"
    output:
        "data/processed/analytics.sqlite"
    shell:
        """
        python scripts/process_data.py \
            --users_csv {input.users} \
            --orders_csv {input.orders} \
            --output_db {output}
        """