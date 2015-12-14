from math import sqrt
N = 2520*2520
p = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20

def factor(n):
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

factors = {}
one_to_twenty = range(11, 21)
candidates = []


for x in xrange(N, p):
    if all(x % n == 0 for n in range(1, 21)):
        print(x)
