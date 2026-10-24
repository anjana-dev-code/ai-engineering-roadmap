"""
PROBLEM:
Plot system performance diagnostics combining two metrics on distinct scales:
- Left Y-Axis: Hourly Request Volume (Bar Chart)
- Right Y-Axis: Error Rate Percentage (Line Plot + Variance Band)
Save figure as 'system_diagnostics.png'.
"""

import matplotlib.pyplot as plt 
import numpy as np 

def plot_system_diagnostics(hours, volume, error_rates):
  # Initialize canvas and primary axis
  fig, ax1 = plt.subplots(figsize=(10, 5))

  # Primary Axis (Left): Request Volume Bar Chart
  ax1.bar(hours, volume, color="#2b5c8f", alpha=0.6, width=0.5, label="Requests")
  ax1.set_xlabel("Hour of Day")
  ax1.set_ylabel("Total Requests", color="#2b5c8f", fontweight="bold")
  ax1.tick_params(axis="y", labelcolor="#2b5c8f")
  ax1.grid(axis="y", linestyle="--", alpha=0.3)

  # Secondary Axis (Right): Error Rate Line Plot
  ax2 = ax1.twinx()
  ax2.plot(
      hours,
      error_rates,
      color="#d9383a",
      marker="o",
      linewidth=2,
      label="Error Rate (%)",
  )
  ax2.set_ylabel("Error Rate (%)", color="#d9383a", fontweight="bold")
  ax2.tick_params(axis="y", labelcolor="#d9383a")

  # Variance band (Safe operating margin)
  mean_err = np.mean(error_rates)
  ax2.fill_between(
      hours,
      mean_err - 1.0,
      mean_err + 1.0,
      color="#d9383a",
      alpha=0.15,
      label="±1% Tolerance",
  )

  # Title & layout management
  plt.title("Production Pipeline: Throughput vs. Error Rate", pad=12)
  plt.tight_layout()
  plt.savefig("system_diagnostics.png", dpi=150)
  plt.close()


if __name__ == "__main__":
  time_stamps = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]
  traffic_counts = [150, 320, 480, 510, 430, 390, 410]
  err_percentages = [1.2, 1.8, 3.9, 5.2, 2.1, 1.9, 2.4]

  plot_system_diagnostics(time_stamps, traffic_counts, err_percentages)
  print("Chart saved successfully as system_diagnostics.png")