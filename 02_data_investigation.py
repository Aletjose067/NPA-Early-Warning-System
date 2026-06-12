import pandas as pd

df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=100000
)

print("\nACCOUNT_CLASS Distribution:")
print(df["ACCOUNT_CLASS"].value_counts())

print("\nUnique ACCOUNT_CLASS Values:")
print(df["ACCOUNT_CLASS"].unique())

print("\nOVERDUE_AMT Statistics:")
print(df["OVERDUE_AMT"].describe())

print("\nSample NPA Records:")
print(
    df[df["ACCOUNT_CLASS"] == "NPA"][
        ["acid", "OVERDUE_AMT", "balance o/s", "ACCOUNT_CLASS"]
    ].head(10)
)