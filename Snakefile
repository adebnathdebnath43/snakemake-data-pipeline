# Snakefile
from datetime import datetime
import os

# Create state folder
#os.makedirs("state", exist_ok=True)

# rule all:
#     input:
#         "data/processed/analytics.sqlite"

# rule validate_input:
#     input:
#         users="data/raw/users.csv",
#         orders="data/raw/orders.csv"
#     output:
#         touch("state/validation_passed.flag")
#     run:
#         # Python script will exit(1) on failure
#         import subprocess, sys
#         result = subprocess.run([
#             "python", "scripts/validation.py",
#             str(input.users), str(input.orders)
#         ])
#         if result.returncode != 0:
#             sys.exit(1)
rule process_data:
    input:
        users="data/raw/users.csv",
        orders="data/raw/orders.csv"
        #flag="state/validation_passed.flag"  # ← DEPENDS ON VALIDATION
    output:
        db="data/processed/analytics.sqlite"
    shell:
        """
        python scripts/process_data.py \
            --users_csv {input.users} \
            --orders_csv {input.orders} \
            --output_db {output.db}
        """