import pandas as pd

df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=100000,
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

print(account_df["ACCOUNT_CLASS"].value_counts())