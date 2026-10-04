"""PROBLEM:
Count the occurrences of each element in a list and return the most 
frequent element (the mode).

Example:
    Input:  ["laptop", "phone", "laptop", "tablet", "laptop", "phone"]
    Output: "laptop"

Simple explaination:
    Keep a tally board (dictionary) of names and votes. Tally every item,
    then find who got the highest vote count.
"""


def find_most_frequent(items: list[str]) -> str:
  counts = {}

  for item in items:
    if item in counts:
      counts[item] += 1  
    else:
      counts[item] = 1  

  best_item = None
  max_count = -1

  for item, count in counts.items():
    if count > max_count:
      max_count = count  
      best_item = item  

  return best_item



if __name__ == "__main__":
  clicks = ["laptop", "phone", "laptop", "tablet", "laptop", "phone"]
  winner = find_most_frequent(clicks)
  print("Most frequent item:", winner)  