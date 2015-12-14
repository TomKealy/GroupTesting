import numpy as np
from collections import Counter
from operator import mul
import pdb

def prime_powers(n):
    return Counter(primes(n))

def count(c):
    return reduce (mul, (c[i] + 1 for i in c))

def triangular_number(n):
    a = prime_powers(n)
    b = prime_powers(n+1)
    c = a + b
    c[2] -= 1
    return c

def primes(n):
    "returns the prime factors of n"x
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

i = 2  
while count(triangular_number(i)) <= 500:
    i += 1
    print i*(i+1)/2

