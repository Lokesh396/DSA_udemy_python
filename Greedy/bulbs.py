def bulbs_cost(A):
    c = 0
    for b in A:
        if c % 2 == 0:
            b = b
        else:
            b = not b

        if b == 0:
            c += 1

    return c


bulbs_A = [1, 0, 0, 1, 1, 0]
print(bulbs_cost(A=bulbs_A))

