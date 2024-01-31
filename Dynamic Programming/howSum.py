def how_sum(targetSum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        difference = targetSum - num
        remainder_Result = how_sum(difference, numbers, memo)
        if remainder_Result is not None:
            remainder_Result.extend([num])
            memo[targetSum] = remainder_Result
            return remainder_Result
    memo[targetSum] = None
    return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [7, 14]))
