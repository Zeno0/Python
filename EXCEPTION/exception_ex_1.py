def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(999)) it creates RecursionError and program crashes

try:
    print(factorial(999))
except (RecursionError, ZeroDivisionError):
    print("EXcePTioN is FOunD IN PRogRAm....")

print("program terminating")
