import heapq
import Queue
from collections import deque

#Takes a list of tuples and returns a tree as a nested tuple
def makeHuffmanTree(symbolTupleList):
    trees = list(symbolTupleList)
    heapq.heapify(trees)
    while len(trees) > 1:
        childR, childL = heapq.heappop(trees), heapq.heappop(trees)
        parent = (childL[0]+childR[0], childL, childR)
        heapq.heappush(trees, parent)
    return trees[0]

def get_codewords(tree, prefix = ' '):
    codes = []
    if len(tree) == 2:
        codes.append((tree[1], prefix))
        return codes
    else:
        get_codewords(tree[1], prefix + '0')
        get_codewords(tree[2], prefix + '1')
    return codes

def children(token, tree):
    children = []
    visited = set()
    to_crawl = deque([token])
    while to_crawl:
        current = to_crawl.popleft()
        if current in visited:
            continue
        visited.add(current)
        node_children = set(tree[current])
        to_crawl.extend(node_children - visited)
    return list(visited)

def printHuffTree(huffTree, prefix = ' '):
    if len(huffTree)==2:
        print(huffTree[1], prefix)
    else:
        printHuffTree(huffTree[1], prefix + '0')
        printHuffTree(huffTree[2], prefix + '1')
       
def leaves(tree):
    result = []
    queue = Queue.Queue()
    queue.put(tree)
    while not queue.empty():
        node = queue.get()
        if type(node[1]) == tuple:
            for subnode in node[2:]:
                queue.put(subnode)
        else:
            result.append(node[1])
    return result

def makeList(tree):
    if len(tree) == 2:
        return [tree[1]]
    left = tree[1]
    right = tree[2]
    return [leaves(left), leaves(right)]

exampleData = [(0.5,'a'), (0.25,'b'), (0.125,'c'), (0.125,'d')]


