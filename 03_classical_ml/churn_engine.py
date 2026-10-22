"""
PROJECT: Automated Customer Churn Classification Engine
"""
import numpy as np
import pandas as pd

def run_churn_pipeline():
    print("Step 1: Generating customer telemetry data...")
    
    # 1. Synthesize customer records
    np.random.seed(42)
    n_samples = 200
    
    raw_data = {
        "customer_id": [f"CUST_{i:03d}" for i in range(1, n_samples + 1)],
        "tenure_months": np.random.randint(1, 48, size=n_samples),
        "monthly_spend": np.random.uniform(20.0, 250.0, size=n_samples),
        "support_calls": np.random.poisson(lam=1.5, size=n_samples),
        "portal_logins_per_week": np.random.exponential(scale=3.0, size=n_samples)
    }
    
    df = pd.DataFrame(raw_data)
    
    print("\nRaw Data Created! Here are the first 3 customers:")
    print(df.head(3))

if __name__ == "__main__":
    run_churn_pipeline()