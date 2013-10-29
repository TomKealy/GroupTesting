#import numpy as np
import HuffSort as hs
from random import randint
from collections import deque

def binary_search(inList):
    low = 0
    high = len(inList)
    loops = 0
    while low+1 < high:
        mid = (low + high) // 2
        upper = inList[mid:high]
        lower = inList[low:mid]
        loops+=1
        if any(lower):
            high = mid
        elif any(upper):
            low = mid
        else:
            # Neither side has a 1
            return -1, loops
    return low, loops

#Simplified algorithm for most unbalanced tree
def huffman_search(node):
    loops = 0 
    return loops

#def huffman_search(tree):
#    loops = 0
#    defective = []
#    to_crawl = deque(hs.group(tree))
#    while to_crawl:
#        print(list(to_crawl))
#        current_branch = to_crawl.popleft() # this is the left branch of the tree
#        branch_sum = sum([t[0] for t in current_branch])
#        if branch_sum !=0 :
#            if(len(current_branch)==1):
#                defective.append(current_branch)
#                exit
#            else:
#                l,r = hs.group(current_branch)
#                to_crawl.extendleft([r])
#                to_crawl.extendleft([l])
#        loops += 1
#    return loops-len(to_crawl),defective
    
#items to search
n = 4
items = [0]*n
position = randint(0,n-1)
items[2] = 1

#probabilities
probs = [2**-(x+1) for x in range(0,n)] #[0.5, 0.25, 0.125, 0.125]# #np.random.dirichlet([1]*n)
non_iid_items = zip(items, probs)

#binary searching the items
defindex, bsloops = binary_search(items)

#huffman searching the items
t = hs.encode(non_iid_items)
hsloops = huffman_search(t)


