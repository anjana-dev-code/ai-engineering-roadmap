"""
PROBLEM:
Compute Mean Squared Error (MSE) between actual targets and predictions.

Formula:
    MSE = (1 / N) * sum((y_pred_i - y_true_i) ** 2)

Example:
    y_true = [100.0, 200.0, 300.0]
    y_pred = [110.0, 190.0, 320.0]
    Output: 200.0
"""

def compute_mse(y_true: list[float], y_pred: list[float]) -> float:
    n = len(y_true)
    if n == 0:
        return 0.0

    total_squared_error = 0.0

    for true_val, pred_val in zip(y_true, y_pred):
        # 1. Difference
        error = pred_val - true_val
        # 2. Square it and accumulate
        total_squared_error += error ** 2

    # 3. Divide by total count (N)
    return total_squared_error / n


if __name__ == "__main__":
    y_true = [100.0, 200.0, 300.0]
    y_pred = [110.0, 190.0, 320.0]

    mse_result = compute_mse(y_true, y_pred)
    print("MSE Result:", mse_result)