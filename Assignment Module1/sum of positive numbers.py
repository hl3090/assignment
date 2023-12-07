"""
 Write a python program to sum of the first n positive integers.

"""


n = int(input("Enter a Number: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1 

print (sum)
