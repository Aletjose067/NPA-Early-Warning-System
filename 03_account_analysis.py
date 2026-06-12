import pandas as pd

df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=100000,
    low_memory=False
)

print("Total Rows:")
print(len(df))

print("\nUnique Customers:")
print(df["custid"].nunique())

print("\nUnique Accounts:")
print(df["acid"].nunique())

print("\nTop 10 Accounts By Transaction Count:")

print(
    df["acid"]
    .value_counts()
    .head(10)
)