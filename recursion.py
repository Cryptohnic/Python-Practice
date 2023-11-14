def factorial(n):
    if n==1: # base case
        return n
    return n*factorial(n-1)

print(f'{factorial(3)}\n')

def fibonacci(n):
    if n==0: # base cases
        return 1
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))