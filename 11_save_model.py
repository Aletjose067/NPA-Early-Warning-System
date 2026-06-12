import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("dataset/processed_accounts.csv")

features = [
    "AGE",
    "SANCT_LIM",
    "OVERDUE_AMT",
    "BALANCE_OS",
    "TOTAL_TRANSACTIONS",
    "TOTAL_TRANSACTION_AMOUNT",
    "AVG_TRANSACTION_AMOUNT"
]

X = df[features]
y = df["TARGET"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

joblib.dump(model, "models/npa_model.pkl")

print("Model Saved Successfully!")