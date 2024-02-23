def max_product(A):
    A.sort()
    prod1 = A[-1] * A[-2] * A[-3]
    prod2 = A[-1] * A[0] * A[1]
    return max(prod1, prod2)


ld = [-3, -5, -9, 4, 3, 2]
print(max_product(ld))