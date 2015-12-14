def digit_sum(n, pow):
    "get the digits of n"
    s = 0
    while n:
        d = n%10
        s += d**pow
        n = n/10
    return s

nums = []
for i in range(10,9999999):
    if i == digit_sum(i, 5):
        nums.append(i)
