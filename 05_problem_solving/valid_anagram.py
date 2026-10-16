"""
PROBLEM: Valid Anagram
Return True if t uses exactly the same letters as s (any order).
Examples: "listen", "silent" -> True 
          "rat", "car" -> False
"""


def is_anagram(s, t):
  # sort the letters of s
  sorted_s = sorted(s)

  # sort the letters of t
  sorted_t = sorted(t)

  # return True if the two sorted results are equal
  return sorted_s == sorted_t


if __name__ == "__main__":
  print(is_anagram("listen", "silent"))  
  print(is_anagram("rat", "car"))  