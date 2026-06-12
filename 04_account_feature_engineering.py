import pandas as pd

# Read sample data
df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=100000,
    low_memory=False
)

# Fill missing overdue amount
df["OVERDUE_AMT"] = df["OVERDUE_AMT"].fillna(0)

# Create account-level dataset
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

print("Account Dataset Shape:")
print(account_df.shape)

print("\nFirst 10 Rows:")
print(account_df.head(10))