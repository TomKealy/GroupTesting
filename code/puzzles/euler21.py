def divisors(n):
    "returns a list of the proper divisors of n"
    divisors = []
    d = 1
    while d < n:
        if n % d == 0:
            divisors.append(d)
        d += 1
    return divisors

def is_amicable(a):
    b = sum(divisors(a))
    if sum(divisors(b)) == a:
        return True
    else:
        return False
    
s = []

timeit
for i in range(10000):
    if sum(divisors(i)) != i:
        if is_amicable(i):
            s.append(i)
            
print sum(s)
timeit
