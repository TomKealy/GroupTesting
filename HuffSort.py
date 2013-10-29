import heapq

'takes a dictionary of symbols and freqs and returns a tree as a nested list'
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

'Sorts into groups based on whether leading char in codeword is 0 or 1. BUG: single coewords are not preserved'
def group(items):
    right = [[item[0],(item[1][1:] if len(item[1])>1 else item[1])] for item in items if item[1].startswith('1')]
    left  = [[item[0],(item[1][1:] if len(item[1])>1 else item[1])] for item in items if item[1].startswith('0')]
    #right = [[item[0],item[1][1:]] for item in right]
    #left  = [[item[0],item[1][1:]] for item in left]

    return left, right

exampleData = [('a',0.5), ('b',0.25), ('c',0.125) , ('d',0.125)]
huffTree = encode(exampleData) 
groups = group(huffTree)
