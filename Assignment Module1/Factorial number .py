# fact = lambda n: [1,0][n>0] or fact (n-1)*n
# print (fact(5))


num = int(input("Enter a Number: "))

fact = 1

while num > 0:
   fact *= num
   num -= 1

print(fact)