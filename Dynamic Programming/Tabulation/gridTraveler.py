def grid_traveler(r, c):
    table = []
    for i in range(r+1):
        col_l = [0] * (c+1)
        table.append(col_l)
    table[1][1] = 1
    for i in range(r+1):
        for j in range(c+1):
            current = table[i][j]
            if i+1 <= r:
                table[i+1][j] += current
            if j+1 <= c:
                table[i][j+1] += current
    return table[r][c]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
