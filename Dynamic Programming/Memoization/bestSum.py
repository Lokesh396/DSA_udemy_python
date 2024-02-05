def best_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder_result = best_sum(target_sum - num, numbers, memo)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
