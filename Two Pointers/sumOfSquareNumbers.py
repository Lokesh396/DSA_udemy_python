import math


def judgeSquareSum(c: int) -> bool:
    r = math.floor(math.sqrt(c))
    l = 0
    while l <= r:
        number = l * l + r * r
        if number == c:
            return True
        elif number < c:
            l += 1
        else:
            r -= 1

    return False

