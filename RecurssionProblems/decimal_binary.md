### Write a program to convert decimal number to binary ?

***Steps***
######*step-1 Recurive case - the flow* 
- Divide the number by 2
- Get the integer quotient for the next iteration
- Get the remainder for the binary digit
- Repeat these steps until the quotient is equal to 1.
$f(n) = n\%2 + 10 * f(n/2)$
######*step-2 Base case - the stopping criteria*
$ n = 0 $
######*step-3 Unintentional case - the constraint*
DectoBin(1.9)??

```python
def DectoBin(number):
    assert int(number) == number , "Only positive integers are allowed"
    if number == 0:
        return 0
    else:
        return number % 2 + (10*DectoBin(int(number / 2)))

decimal = int(input("Enter the decimal number: "))
print(DectoBin(number=decimal))
```