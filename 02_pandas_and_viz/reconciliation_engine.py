"""
PROBLEM:
Reconcile payment logs between internal records and payment gateways.
Calculate amount differences, apply tiered conditional audit flags,
and extract records needing investigation.

Rules:
    - CRITICAL_MISMATCH: difference > 5.0 OR status == 'FAILED'
    - MINOR_DISCREPANCY: 0.0 < difference <= 5.0
    - CLEAN: difference == 0.0 AND status == 'SETTLED'
"""

import numpy as np 
import pandas as pd 

def reconcile_transactions(df):
    # Calculate absolute discrepancy between systems
    df["diff"] = (df["internal_amount"]- df["gateway_amount"]).abs()

    # Define boolean audit conditions
    crit_condition = (df["diff"] > 5.0) | (df["status"] == "Failed")
    minor_condition = (df['diff'] > 0.0) & (df["diff"] <= 5.0)

    # Vectorized assignment using np.select
    conditions = [crit_condition, minor_condition]
    choices = ["CRITICAL_MISMATCH", "MINOR_DISCREPANCY"]
    df["audit_flag"] = np.select(conditions, choices, default="CLEAN")

    # Filter out clean transactions and sort by largest diff
    discrepancies = df[df["audit_flag"]!= "CLEAN"].sort_values(
        by = "diff", ascending = False
    )

    return discrepancies

if __name__ == "__main__":
    sample_data = {
        "txn_id": ["TXN_101", "TXN_102", "TXN_103", "TXN_104", "TXN_105"],
        "internal_amount": [120.00, 45.50, 310.00, 80.00, 15.00],
        "gateway_amount": [120.00, 43.00, 250.00, 80.00, 15.00],
        "status": ["SETTLED", "SETTLED", "SETTLED", "FAILED", "SETTLED"],
    }

    raw_df = pd.DataFrame(sample_data)
    audit_results = reconcile_transactions(raw_df)

    print("Transactions Requiring Audit")
    print(audit_results[["txn_id", "diff", "status", "audit_flag"]].to_string(index=False))


