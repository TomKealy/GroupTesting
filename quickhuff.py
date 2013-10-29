from collections import deque
from random import uniform
import HuffSort as hs

#' ' => did not find defective
def huff_search(node):
    loops = 0
    to_test = deque(node)
    while to_test:
        loops+=1
        current = to_test.popleft()
        if current[0]==1 or loops == 3:
            return loops
    return ' '

def full_huff_search(tree):
    loops = 0
    to_test = deque(hs.group(tree))
    #defective = 0
    while to_test:
        #print('in here')
        loops+=1
        current = to_test.popleft()
        branch_sum = sum([t[0] for t in current])
        if branch_sum != 0:
            return loops
        else:
            l,r = hs.group(current)
            to_test.extendleft([r])
            to_test.extendleft([l])
    return 0

def sample_non_uniform():
    choice = 0
    u = uniform(0,1)
    if u < 0.5:
        choice = 0
    elif u >= 0.5 and u < 0.75:
        choice = 1
    elif u >= 0.75 and u < 0.875:
        choice = 2
    else:
        choice = 3
    return choice
 
#possible huffman trees
a=[[1,'1'],[0,'00'],[0,'100'],[0,'101']]
b=[[0,'1'],[1,'00'],[0,'100'],[0,'101']]
c=[[0,'1'],[0,'00'],[1,'100'],[0,'101']]
d=[[0,'1'],[0,'00'],[0,'100'],[1,'101']]

choices = [a,b,c,d]
hloops = []
tests = 100000
for x in range(0,tests):
    choice = sample_non_uniform()
    tree =  choices[choice]
    hloops.append(full_huff_search(tree))

print(sum(hloops))
av = float(sum(hloops))/len(hloops)
print(av)
