"""
 Write a Python program to get a single string from two given strings,separated by a space and swap the first two 
 characters of each string.

"""


s1 = input("Enter string: ")
s2 = input("Enter 2nd string: ")

s3 = s1[2:] + s2 + s1[:-2]

print(s3)



