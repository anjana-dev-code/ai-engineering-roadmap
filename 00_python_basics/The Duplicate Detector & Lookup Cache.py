"""PROBLEM:
Find and return the very first item that appears more than once in a list.
If no items repeat, return -1.

Example:
    Input:  [101, 204, 305, 101, 409]
    Output: 101

"""


def find_first_duplicate(ids):
  seen = set()

  for item in ids:
    if item in seen:
      return item
    seen.add(item)

  return -1


# --- Quick Test ---
if __name__ == "__main__":
  numbers = [101, 204, 305, 101, 409, 204, 550]
  print("Result:", find_first_duplicate(numbers))