import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load processed dataset
df = pd.read_csv("dataset/processed_accounts.csv")

# Features
X = df[
    [
        "AGE",
        "SANCT_LIM",
        "OVERDUE_AMT",
        "BALANCE_OS",
        "TOTAL_TRANSACTIONS",
        "TOTAL_TRANSACTION_AMOUNT",
        "AVG_TRANSACTION_AMOUNT"
    ]
]

# Target
y = df["TARGET"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train
rf.fit(X_train, y_train)

# Prediction
y_pred = rf.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))