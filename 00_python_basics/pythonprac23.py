import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score

# Step 1: Synthesize Tabular Records
np.random.seed(42)
n_samples = 200

tenure = np.random.randint(1, 60, size=n_samples)
monthly_charges = np.random.uniform(20.0, 120.0, size=n_samples)
support_tickets = np.random.poisson(lam=2, size=n_samples)

# Probabilistic Churn Formula
log_odds = -2.0 - (0.05 * tenure) + (0.02 * monthly_charges) + (0.4 * support_tickets)
prob_churn = 1 / (1 + np.exp(-log_odds))
churn = (prob_churn > 0.5).astype(int)

dataset = pd.DataFrame({
    "tenure": tenure,
    "monthly_charges": monthly_charges,
    "support_tickets": support_tickets,
    "churn": churn
})

# Step 2: Separate Targets & Partitions
X = dataset.drop(columns=["churn"])
y = dataset["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Step 3: Feature Scaling & Model Execution
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use transform() on test, never fit_transform()

clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)

# Step 4: Metric Benchmarking
y_preds = clf.predict(X_test_scaled)
y_probs = clf.predict_proba(X_test_scaled)[:, 1]

print(f"ROC-AUC Score: {roc_auc_score(y_test, y_probs):.4f}")
print(f"Macro F1-Score: {f1_score(y_test, y_preds):.4f}")

# Step 5: Feature Coefficient Inspection
importance = pd.DataFrame({
    "Feature": X.columns,
    "Weight": clf.coef_[0]
}).sort_values(by="Weight", ascending=False)

print("\nFeature Impact on Churn Risk:")
print(importance.to_string(index=False))