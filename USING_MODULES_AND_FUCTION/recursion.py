def fact(n):
    res= 1
    if n >1:
        for i in range(2,n+1):
            res *=i
    return res

# recursive approach
def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    if n  == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        val1= 1
        val2= 0
        for i in range(1, n+1):
            res= val2+val1
            val2= val1
            val1= res
    return res

print(fact(23))
print("-"*50)
print(factorial(23))
print("-"*50)
print(fib(29))
print(fib(30))
print(fib(31))
print(fib(32))
print("-"*50)
print(fibonacci(29))
print(fibonacci(30))
print(fibonacci(31))
print(fibonacci(32))
