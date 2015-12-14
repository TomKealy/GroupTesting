from collections import deque

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def rotate(l,n):
    return l[n:] + l[:n]

def circular(n):
    "takes a string and generates all circ rotations"
    len_ = len(n)
    rotations = []
    for i in range(len_):
        n = rotate(n, 1)
        rotations.append(n)
    return rotations

def main():
    lim = 1000
    primes = sundaram3(lim)
    count = 0
    reject = ['0', '2', '4', '5', '6', '8']
    for p in primes:
        if str(p) in reject:
            primes.remove(p)
        
if __name__ == "__main__":
    main()
