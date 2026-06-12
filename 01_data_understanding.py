import pandas as pd

# Read only first 10000 rows
df = pd.read_csv(
    "dataset/data.txt",
    sep="|",
    nrows=10000
)

print("Shape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nACCOUNT_CLASS Values:")
print(df["ACCOUNT_CLASS"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())