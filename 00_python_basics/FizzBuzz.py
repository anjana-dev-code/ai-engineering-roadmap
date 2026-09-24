"""Problem 2 (Basic)

Write a program that prints all numbers from 1 to 50, but:

for multiples of 3, print "Fizz" instead of the number
for multiples of 5, print "Buzz" instead of the number
for numbers that are multiples of both 3 and 5, print "FizzBuzz" """

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    



