def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def num_digits(n):
    digits = 0
    while n:
        digits += 1
        n = n/10
    return digits

fibs = [0, 1]
nd = 0

for i in range(2, 5000):
    fibs.append(fibs[i-1] + fibs[i-2])
    if num_digits(fibs[i]) == 1000:
        break

