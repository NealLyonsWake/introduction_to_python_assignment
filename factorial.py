"""
Write a Python function to compute the factorial of a number factorial(n).
Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120, etc.
If the number given is negative, the function should return None.
"""

def factorialize(n):
    if n <= 0:
        return None
    factor = 1
    for i in range (1, n+1):
        factor = factor * i
    return factor
   
print(factorialize(5))