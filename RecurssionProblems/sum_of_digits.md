
### Write a program to find sum of the digits of a number ?

***Steps***
######*step-1 Recurive case - the flow* 
$f(n) = n\%10 + f(n//10)$
######*step-2 Base case - the stopping criteria*
$ n = 0$
######*step-3 Unintentional case - the constraint*
sumOfDigits(-12)??
sumOfDigits(23.2)??

```python
def sumOfDigits(number):
    assert (int(number) == number and number >= 0), 'Only positive integers are allowed'
    if(number == 0):
        return 0
    else:
       return (number % 10) + sumOfDigits(number//10)
    
number = int(input("Enter a number: "))
print("sum of digits of number", number, "is", sumOfDigits(number=number))
```