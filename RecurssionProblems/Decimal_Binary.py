def decimal_binary(num, res=""):
    if num == 0:
        return int(res)
    res = str(num % 2) + res
    return decimal_binary(num // 2, res)


print(decimal_binary(64))