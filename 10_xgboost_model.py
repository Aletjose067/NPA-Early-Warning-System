import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from xgboost import XGBClassifier

# Load data
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

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# XGBoost
xgb = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    eval_metric="logloss"
)

# Train
xgb.fit(X_train, y_train)

# Predict
y_pred = xgb.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))