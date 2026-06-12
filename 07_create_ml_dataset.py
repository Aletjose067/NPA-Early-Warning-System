import pandas as pd

df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=1000000,
    low_memory=False
)

df["OVERDUE_AMT"] = df["OVERDUE_AMT"].fillna(0)

account_df = df.groupby("acid").agg(
    AGE=("AGE", "first"),
    SANCT_LIM=("SANCT_LIM", "first"),
    OVERDUE_AMT=("OVERDUE_AMT", "max"),
    BALANCE_OS=("balance o/s", "first"),
    ACCOUNT_CLASS=("ACCOUNT_CLASS", "first"),
    TOTAL_TRANSACTIONS=("TRAN_AMT", "count"),
    TOTAL_TRANSACTION_AMOUNT=("TRAN_AMT", "sum"),
    AVG_TRANSACTION_AMOUNT=("TRAN_AMT", "mean")
).reset_index()

# Create target
account_df["TARGET"] = account_df["ACCOUNT_CLASS"].apply(
    lambda x: 1 if x in ["SMA-1", "SMA-2", "NPA"] else 0
)

print(account_df["TARGET"].value_counts())

# Save processed dataset
account_df.to_csv(
    "dataset/processed_accounts.csv",
    index=False
)

print("\nSaved Successfully!")