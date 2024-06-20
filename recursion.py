# Factorial of number
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(7))

# Fibonacci Sequence
a = int(input("Enter number:"))

def fibonacciSequence(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fibonacciSequence(n-1) + fibonacciSequence (n-2)

for i in range(a):
    print(fibonacciSequence(i))