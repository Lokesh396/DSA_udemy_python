def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                current = i + num
                if current < len(table):
                    arr = [] + table[i]
                    arr.append(num)
                    table[current] = arr
    return table[target_sum]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))