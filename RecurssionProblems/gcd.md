
### Calculate gcd of two numbers ?

***Steps***
######*step-1 Recurive case - the flow* 
$gcd(a, b) = gcd(b, a\%b)$
######*step-2 Base case - the stopping criteria*
$ b = 0$
######*step-3 Unintentional case - the constraint*
positive integers
convert negative numbers to positive

```python
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

```