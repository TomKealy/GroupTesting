import time


def profile(function):
    """ intended to be used as decorator for a function or a method to check
        the execution time 
    from http://code.activestate.com/recipes/577329-some-prime-generation-algorithms/
    """

    def decorate(args):
        """ concrete decorator measuring the execution time of
            given function or method """
        start = time.clock()
        result = function(args)
        print("...profiling of '%s': tooks %f seconds" % \
              (function.__name__, time.clock()-start))
        return result
    return decorate


@profile
def sundaram(n):
    """Sundaram's sieve to find othe primes up to 2n+1"""
    limit = n+1
    nums = range(3, limit/2, 2)
    sieve = [True] * limit
    sieve[1] = False

    # remove all numbers of the form i + j + 2ij
    # 1 <= i <= j
    # i + j + 2ij <= n
    
    for j in range(1, limit/2):
        f = 2*j+1
        for i in range(1, j):
            num = i*f + j
            if num in nums:
                nums.remove(num)

    # double the remaining numbers and increment by one
    nums = [2*k+1 for k in nums]
    return nums
    #return [2, 3] + [2*k+1 for k in range(1, n//2) if sieve[k]]


def main():
    primes_one_hundred = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for i in sundaram(100):
        if i not in primes_one_hundred:
            print i

if __name__ == '__main__':
    main()
