s1 = input("Enter a string:")

if len(s1)<2:
    print ("empty string")
else:
    s2 = s1[2:] + s1[::-2] 
    print(s2)   