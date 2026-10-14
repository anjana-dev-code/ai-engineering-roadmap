"""
PROBLEM: Two Sum

Given a list of integers `nums` and an integer `target`, return the
positions (indices) of the two numbers that add up to `target`.

Rules:
- Exactly one valid pair exists.
- You can't use the same element twice.
- Return the positions in a list, e.g. [0, 1].

Examples:
    nums = [2, 7, 11, 15], target = 9   ->  [0, 1]   (2 + 7 = 9)
    nums = [3, 2, 4],      target = 6   ->  [1, 2]   (2 + 4 = 6)

Approach: hash map (dict). Walk the list once, store each number's
position, and for each new number check if its complement
(target - number) has already been seen.
"""

def two_sum(nums, target):
    # make an empty dict to remember numbers I have seen
    seen = {}

    # go through the list, tracking each number and its position
    for i, num in enumerate(nums):
        # work out the complement
        complement = target - num 

        # if the complement is in the dict: return both positions
        if complement in seen:
            return [seen[complement], i]
        
        # otherwise store this number and its position, move on
        seen[num] = i

print(two_sum([2,7,10,11,15,20,25,30],30))

    
