"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

"""


# solution 1

def tribonacci1(n: int) -> int:
    if n == 0:
        return 0
    res = [0, 1, 1]
    for i in range(n - 2):
        s = res[0] + res[1] + res[2]
        res[0] = res[1]
        res[1] = res[2]
        res[2] = s

    return res[2]


# solution 2

def tribonacci2(n: int) -> int:
    res = [0, 1, 1]
    for i in range(n - 2):
        s = res[-1] + res[-2] + res[-3]
        res.append(s)

    return res[n]
