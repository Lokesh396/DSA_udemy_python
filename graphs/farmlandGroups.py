"""
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a
hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These
rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally
 adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner
of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group
of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length
array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no
groups of farmland, return an empty array. You may return the answer in any order.
"""


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        visited = set()
        r1, c1 = [0], [0]

        def island(i, j):
            if i < 0 or j < 0 or i >= len(land) or j >= len(land[0]) or land[i][j] == 0:
                return False
            if (i, j) in visited:
                return False
            r1[0] = max(i, r1[0])
            c1[0] = max(j, c1[0])
            visited.add((i, j))
            island(i + 1, j)
            island(i - 1, j)
            island(i, j + 1)
            island(i, j - 1)
            return (r1[0], c1[0])

        out = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                temp = island(i, j)
                if temp:
                    out.append([i, j, temp[0], temp[1]])
                r1[0] = 0
                c1[0] = 0
        return out