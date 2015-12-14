from math import sqrt


def factor(n):
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

palindromes = []

factors = {}

candidates = []

for x in range(100000, 1000000):
    s = str(x)
    if s == s[::-1]:
        palindromes.append(x)

for p in palindromes:
    f = [r for r in factor(p) if r >= 100 and r <= 999]
    if len(f) > 1:
        for i in range(0, len(f)):
            for j in range(i+1, len(f)):
                if f[i]*f[j] in palindromes:
                    candidates.append(f[i]*f[j])
