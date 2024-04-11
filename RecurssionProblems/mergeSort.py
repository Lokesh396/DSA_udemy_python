
def merge(data, start, mid, end):
    l1 = data[start:mid]
    l2 = data[mid:end]

    i, j = 0, 0
    print(start, mid, end, l1, l2)
    for i in range(len(l1)):
        if l1[i] <= l2[j]:
            data[start+i] = l1[i]

        else:
            data[start+i] = l2[j]
            j += 1


def merge_sort(data, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(data, start, mid)
        merge_sort(data, mid+1, end)
        merge(data, start, mid, end)


array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(merge_sort(array, 0, len(array)-1))