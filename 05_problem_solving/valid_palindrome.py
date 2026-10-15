"""
PROBLEM: Valid Palindrome

Given a string s, return True if it reads the same forwards and
backwards, otherwise False.

Examples:
    "madam"  ->  True
    "hello"  ->  False
"""

def is_palindrome(s):
    # make a reversed copy of s
    reversed_s = s[::-1]

    # compare s with the reversed copy and return True if they match
    return s == reversed_s

print(is_palindrome("madam"))   
print(is_palindrome("hello"))   

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(is_palindrome(word))
