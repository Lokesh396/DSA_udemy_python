def sum_natural_numbers(number):
    if number == 1:
        return 1
    return number + sum_natural_numbers(number-1)


print(sum_natural_numbers(10))
