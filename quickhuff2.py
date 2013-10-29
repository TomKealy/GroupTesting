import heapq
from random import randint
from collections import deque

def encode(symbfreq):
    tree = [[wt, [sym, ""]] for sym, wt in symbfreq]
    heapq.heapify(tree)
    while len(tree)>1:
        lo, hi = heapq.heappop(tree), heapq.heappop(tree)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(tree, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(tree)[1:], key=lambda p: (len(p[-1]), p))
   
#' ' => did not find defective
def huff_search(node):
    loops = 0
    to_test = deque(node)
    while to_test:
        loops+=1
        current = to_test.popleft()
        if current[0]==1:
            return loops
    return ' '

a = [(1,0.5),(0,0.25),(0,0.125),(0,0.125)]

b = [(0,0.5),(1,0.25),(0,0.125),(0,0.125)]

c = [(0,0.5),(0,0.25),(1,0.125),(0,0.125)]

d = [(0,0.5),(0,0.25),(0,0.125),(1,0.125)]

choices = [a,b,c,d]
hloops = []
tests = 1000
for x in range(0,tests):
    c = randint(0,3)
    choice = choices[c]
    tree =  encode(choice)
    hloops.append(huff_search(tree))

print(sum(hloops))
av = float(sum(hloops))/len(hloops)
print(av)







