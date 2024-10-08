"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(arr, res, subset, index):
            res.append(subset[:])
            for i in range(index, len(arr)):
                subset.append(arr[i])
                sub(arr, res, subset, i +1)
                subset.pop()
        res = []
        subset = []
        sub(nums, res, subset, 0)
        return res
