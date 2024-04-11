"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""


def containsDuplicate(nums):
    ls = set()
    for i in nums:
        if i in ls:
            return True
        ls.add(i)
    return False


arr = [x for x in range(1, 100)]
print(containsDuplicate(arr))
arr.append(5)
print(containsDuplicate(arr))



