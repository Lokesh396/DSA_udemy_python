def grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    key = str(m)+','+str(n)
    if key in memo:
        return memo[key]
    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]


rows = int(input("Enter row size: "))
cols = int(input("Enter col size: "))
print(grid_traveler(m=rows, n=cols))
