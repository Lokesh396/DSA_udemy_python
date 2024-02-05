def fib(n, memo=None):
    if memo is None:
        memo = dict()
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    # print(memo)
    return memo[n]


fib_n = int(input("Enter n value: "))
print(fib(fib_n))
