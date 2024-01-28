def DectoBin(number):
    if number == 0:
        return 0
    else:
        return number % 2 + (10*DectoBin(int(number / 2)))

decimal = int(input("Enter the decimal number: "))
print(DectoBin(number=decimal))