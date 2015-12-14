def collatz(n, table = {}):
    "returns a list of the collatz seq of n"
    coll = []
    while n not in coll:
        if n in table:
            table.update({x: coll[i:] for i, x in enumerate(coll)})
            return coll + table[n]
        elif n % 2 == 0:
            coll.append(n)
            n = n//2
        else:
            coll.append(n)
            n = 3*n+1
    table.update({x: coll[i:] for i, x in enumerate(coll)})
    return coll

lengths = []
for i in range(1000000):
    lengths.append((i, len(collatz(i))))
