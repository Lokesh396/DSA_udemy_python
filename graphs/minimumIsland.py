grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w']
]

def counter(grid, r, c, visited):
    rowInBounds = 0 <= r and r < len(grid)
    colInBounds = 0 <= c and c < len(grid[0])
    if not colInBounds or not rowInBounds:
        return 0
    if grid[r][c] == 'w': return 0
    pos = str(r) + ',' + str(c)
    if pos in visited: return 0
    visited.add(pos)
    size = 1
    size += counter(grid=grid, r= r - 1, c = c, visited=visited)
    size += counter(grid=grid, r= r + 1, c = c, visited=visited)
    size += counter(grid=grid, r= r, c = c + 1, visited=visited)
    size += counter(grid=grid, r= r, c = c - 1, visited=visited)

    return size

def minimumIslandCount(grid):
    visited = set()
    count = len(grid) * len(grid[0]) + 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = counter(grid=grid, r=r,c=c, visited=visited)
            if size  != 0:
                count = min(count, size)

    return count

print(minimumIslandCount(grid=grid))