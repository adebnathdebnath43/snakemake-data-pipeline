<!-- Your task is to build a small, reproducible data pipeline using Snakemake and Python. The pipeline should read data from two CSV files, merge them, and load the result into a SQLite database.

### **Project Structure**

You will be given the following starter files:

```
.
├── data
│   └── raw
│       ├── orders.csv
│       └── users.csv
└── README.md  (This file)
```

### **Requirements**

1.  **Create a Python script** (e.g., `scripts/process_data.py`) that performs the following:

      * Accepts paths for the two input CSVs and one output SQLite database.
      * Reads `data/raw/users.csv` into a pandas DataFrame.
      * Reads `data/raw/orders.csv` into a pandas DataFrame.
      * Performs an **inner join** on the two DataFrames using the `user_id` column.
      * Writes the resulting merged DataFrame to a new table named `user_orders` inside a SQLite database file.
      * **Important:** The script should be modular. It should not have hardcoded file paths.

2.  **Create a `Snakefile`** that orchestrates this process.

      * The `Snakefile` should define the inputs (`users.csv`, `orders.csv`) and the final output (`data/processed/analytics.sqlite`).
      * It should have a rule that executes your Python script, passing the correct input and output file paths to it.
      * The pipeline must be executable by running a single `snakemake` command from the root directory.

3.  **Create a `requirements.txt`** file listing all necessary Python libraries (e.g., `pandas`, `snakemake`).

4.  **Create a GitHub Repo** and commit the entire project. 

### **Final Deliverable**

The final repo structure should look something like this:

```
.
├── data
│   ├── raw
│   │   ├── orders.csv
│   │   └── users.csv
│   └── processed   <-- This directory and file will be created by your pipeline
│       └── analytics.sqlite
├── scripts
│   └── process_data.py
├── Snakefile
├── requirements.txt
└── README.md
```

To be clear, there are only three files that need to be created:

  * `Snakefile`
  * `scripts/process_data.py`
  * `requirements.txt`

----- -->