import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("dataset/processed_accounts.csv")

# Features
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

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

# Feature importance
importance = pd.DataFrame({
    "Feature": features,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

# Plot
plt.figure(figsize=(8,5))
plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.tight_layout()
plt.show()