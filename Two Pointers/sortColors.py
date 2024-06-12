def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    l = 0
    m = 0
    r = len(nums) - 1
    while m <= r:
        if nums[m] == 0:
            nums[m], nums[l] = nums[l], nums[m]
            l += 1
            m += 1
        elif nums[m] == 2:
            nums[r], nums[m] = nums[m], nums[r]
            r -= 1
        else:
            m += 1


arr = [0, 2, 1, 1, 0, 2]
sortColors(arr)
print(arr)
