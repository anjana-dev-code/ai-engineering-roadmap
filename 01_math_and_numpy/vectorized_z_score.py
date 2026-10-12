"""
PROBLEM: Vectorized Z-Score Outlier Extraction
Normalize a 1D NumPy array of numerical readings and filter out anomalous spikes
where the absolute Z-score exceeds a given threshold.
Formula:
    Z = (X - mean) / std

Example:
    Input:  np.array([45.0, 52.0, 48.0, 98.0, 50.0, 47.0, 110.0, 53.0])
    Outliers (|Z| > 2.0): [98.0, 110.0]
"""
import numpy as np 

def extract_outliers(readings, threshold=2.0):
    # Compute global statistical baselines
    mean_val = np.mean(readings)
    std_val = np.std(readings)
    
    # Safety guard against zero division if all values are identical
    if std_val == 0:
        return np.array([])
        
    # Vectorized Z-score calculation across the entire array
    z_scores = (readings - mean_val) / std_val
    
    # Boolean masking to isolate outlier elements
    outlier_mask = np.abs(z_scores) > threshold
    return readings[outlier_mask]

if __name__ == "__main__":
    cpu_readings = np.array([45.0, 52.0, 48.0, 98.0, 50.0, 47.0, 110.0, 53.0])
    detected = extract_outliers(cpu_readings)
    print("Detected Outliers:", detected)