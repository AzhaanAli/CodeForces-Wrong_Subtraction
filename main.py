"""
DIRECTIONS:
Decrement a number k times with a wrong sort of subtraction.
If the number has 0 as its final digit, divide by ten.
If a number does not have 0 as its final digit, subtract 1.

Given an initial number and a number k - how many times to "subtract," print the resultant number.
"""

userInputs = input().split(' ')
n = int(userInputs[0])
k = int(userInputs[1])

for i in range(0, k):
    n = n / 10 if n % 10 == 0 else n - 1

print(int(n))
