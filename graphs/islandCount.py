grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w']
]


def visitLand(grid, r, c, visited):
    rowInBounds = 0 <= r and r < len(grid)
    colInBound = 0 <= c and c < len(grid[0])
    if (not rowInBounds or not colInBound): return False
    if (grid[r][c] == 'w'): return False
    pos = str(r) + ',' + str(c)
    if pos in visited: return False
    visited.add(pos)
    visitLand(grid=grid, r=r - 1, c=c, visited=visited)
    visitLand(grid=grid, r=r + 1, c=c, visited=visited)
    visitLand(grid=grid, r=r, c=c - 1, visited=visited)
    visitLand(grid=grid, r=r, c=c + 1, visited=visited)
    return True


def calculateIslands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if visitLand(grid, r, c, visited):
                count += 1

    return count


print(calculateIslands(grid=grid))
