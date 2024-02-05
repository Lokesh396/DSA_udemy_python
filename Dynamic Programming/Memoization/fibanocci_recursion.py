def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


fib_n = int(input("Enter the n: "))
print(fib(fib_n))
 