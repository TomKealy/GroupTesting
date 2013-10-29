import heapq
from random import randint

def encode2(symbfreq):
    tree = list(symbfreq)
    heapq.heapify(tree)
    while len(tree)>1:
        lo, hi = heapq.heappop(tree), heapq.heappop(tree)
        parent = (lo[0] + hi[0], lo, hi)
        heapq.heappush(tree, parent)
    return tree[0]

def printHuffTree(huffTree, prefix = ' '):
    if len(huffTree)==2:
        print(huffTree[1], prefix)
    else:
        printHuffTree(huffTree[1], prefix + '0')
        printHuffTree(huffTree[2], prefix + '1')

def huff_search_recursive(node,rounds=0):
    if len(node)==2:
        if node[1]==1:
            print rounds
    else:
        rounds += 1
        rounds += huff_search_recursive(node[1],rounds)
        rounds += huff_search_recursive(node[2],rounds)

a = [(0.5,1),(0.25,0),(0.125,0),(0.125,0)]
b = [(0.5,0),(0.25,1),(0.125,0),(0.125,0)]
c = [(0.5,0),(0.25,0),(0.125,1),(0.125,0)]
d = [(0.5,0),(0.25,0),(0.125,0),(0.125,1)]

choices = [a,b,c,d]
hloops = []
tests = 10
for x in range(0,tests):
    num = randint(0,3)
    choice = choices[num]
    tree =  encode2(choice)
    hloops.append(huff_search_recursive(tree))

print(sum(hloops))
av = float(sum(hloops))/tests
print(av)

































