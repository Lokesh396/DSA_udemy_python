### Write a program to calculate power of a number ?

***Steps***
######*step-1 Recurive case - the flow* 
$f(n, p) = n + f(n, p-1)$
######*step-2 Base case - the stopping criteria*
$ p = 1 $
######*step-3 Unintentional case - the constraint*
powerOfN(-12, 1)??
powerOfN(23.2, -2)??

```python
def powerOfN(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    else:
        return base * powerOfN(base=base, power= power - 1)

values = list(map(int, input("Enter base and power with space between: ").split()))
print(powerOfN(values[0], values[1]))
```