def binary_search(b_array, start, end, target):
    if end < start:
        return None
    mid = (start+end) // 2
    if b_array[mid] == target:
        return mid
    if target < b_array[mid]:
        return binary_search(b_array, start, mid-1, target)
    return binary_search(b_array, mid+1, end, target)


binary_array = [-1, 0, 1, 3, 5, 6, 9, 10, 12]
print(binary_search(binary_array, 0, len(binary_array)-1, 10))
