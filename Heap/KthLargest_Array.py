# 215. Kth largest Element in an Array.

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]


# It's other variant where the elements are strings.


"""
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
"""
class Solution1:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(num) for num in nums]
        heapq.heapify(nums)
        while k-1 > 0:
            heapq.heappop(nums)
            k -= 1
        return str(-nums[0])
