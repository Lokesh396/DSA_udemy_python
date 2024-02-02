def best_sum(target_sum, numbers):
    table = [None] * (target_sum+1)
    table[0] = []
    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                current = i + num
                if current < len(table):
                    arr = [] + table[i]
                    arr.append(num)
                    if table[i+num] is not None:
                        if len(table[i+num]) > len(arr):
                            table[i+num] = arr
                    else:
                        table[i+num] = arr

    return table[target_sum]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
