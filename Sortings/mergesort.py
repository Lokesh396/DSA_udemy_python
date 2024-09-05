def merge(arr, p, q, r):
    left_arr = arr[p:q+1]
    right_arr = arr[q+1:r+1]
    i, j, k = 0, 0, p
    la_len = len(left_arr)
    ra_len = len(right_arr)
    while i < la_len and j < ra_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < la_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < ra_len:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        q = p + (r-p) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


inpt_arr = list(map(int, input().split()))
merge_sort(inpt_arr, 0,  len(inpt_arr)-1)
print(f"Sorted Array: {inpt_arr}")
