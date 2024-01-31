def can_sum(targetSum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if can_sum(targetSum - num, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 3, 5]))
print(can_sum(7, [1]))
print(can_sum(300, [7, 14]))
