def calculate_max_size(A):
    A.sort(key=lambda x: x[1])
    prev_s, prev_e = A[0]
    count = 1
    for s, e in A:
        if s <= prev_e:
            pass
        else:
            prev_s, prev_e = s, e
            count += 1

    return count


ld = [[1, 2], [2, 10], [4, 6]]
print(calculate_max_size(ld))
