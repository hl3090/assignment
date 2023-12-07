n = int(input("Enter the range of Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series of given range:")

while n:
    print(a, end=" ")
    a, b = b, a + b
    n -= 1