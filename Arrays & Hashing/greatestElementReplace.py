"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.
"""


def replace_elements(nums):
    mx = -1
    for i in range(len(nums)-1, -1, -1):
        temp = nums[i]
        nums[i] = mx
        mx = max(temp, mx)
    return nums


print(replace_elements([17, 18, 5, 4, 6, 1]))