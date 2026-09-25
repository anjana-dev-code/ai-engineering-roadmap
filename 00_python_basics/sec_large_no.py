"""
You're given a list of numbers: [12, 7, 19, 3, 25, 8, 14]
Write code that finds and prints the second largest number in the list 
— without sorting the list and without using max() twice."""

nums = [12, 7, 19, 3, 25, 8, 14]

largest = second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest:
        second_largest = n

print(second_largest)