"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memory = {}
        def pathSum(i, j):
            if i == len(matrix) - 1:
                return matrix[i][j]
            if (i, j) in memory:
                return memory[(i, j)]
            x = pathSum(i + 1, max(0, j - 1))
            y = pathSum(i + 1, j)
            z = pathSum(i + 1, min(len(matrix[0]) - 1, j + 1))
            
            memory[(i, j)] = matrix[i][j] + min(x, y, z)
            return memory[(i, j)]

        min_sum = float('inf')
        for j in range(len(matrix[0])):
            min_sum = min(min_sum, pathSum(0, j))
        
        return min_sum

        return min_
