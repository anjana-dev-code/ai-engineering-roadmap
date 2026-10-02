"""PROBLEM:
Read a training log file line-by-line using a context manager.
Extract and return a list of epoch numbers where loss > threshold.

Example Input:
    epoch:1,loss:0.854
    epoch:2,loss:0.412
Output (threshold=0.5):
    [1]
"""
import os

def extract_high_loss_epochs(
    filepath: str, threshold: float = 0.5
) -> list[int]:
  high_loss_epochs = []

  with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
      clean_line = line.strip()
      if not clean_line:
        continue

      parts = clean_line.split(",")
      epoch_num = int(parts[0].split(":")[1])
      loss_val = float(parts[1].split(":")[1])

      if loss_val > threshold:
        high_loss_epochs.append(epoch_num)

  return high_loss_epochs



if __name__ == "__main__":
  # Automatically points to the directory containing this script
  base_dir = os.path.dirname(os.path.abspath(__file__))
  log_file = os.path.join(base_dir, "train_log.txt")

  # 1. Guarantee sample data exists right next to this script
  with open(log_file, "w", encoding="utf-8") as f:
    f.write("epoch:1,loss:0.854\n")
    f.write("epoch:2,loss:0.621\n")
    f.write("epoch:3,loss:0.412\n")
    f.write("epoch:4,loss:0.195\n")

  # 2. Run the parser
  results = extract_high_loss_epochs(log_file, threshold=0.5)
  print("High loss epochs:", results)