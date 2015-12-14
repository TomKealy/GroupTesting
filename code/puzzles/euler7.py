def primes(a):
    for x in a:
        comp = []
        for y in a:
            comp.append(x*y)
        for z in comp:
            if z in a:
                a.remove(z)
    return a


def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
