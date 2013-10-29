import math
import numpy as np
import huffman0 as h

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
 
#def group_by_probability(xs, start=1):
#    last_sum = 0
#    for stop, acc in enumerate(np.add.accumulate(xs), start):
#        if acc - last_sum >= 1:
#            yield list(range(start, stop))
#            last_sum = acc
#            start = stop
#    if start < stop:
#        yield list(range(start, stop))    

def group_by_probability(xs, start=1):    
    xs = np.add.accumulate(xs)
    idxs = np.searchsorted(xs, np.arange(xs[-1]) + 1, side='left').tolist()
    return [list(range(i+start, j+start)) for i, j in zip([0] + idxs, idxs)]
 
#finds the defectives but outputs 21 instead of 789 (as 3*256 = 768)
def HGBSA(inList, num_defectives):

    n = len(inList)
    defectives = []
  
    start = 0    
    loops = 0
    while num_defectives > 0:

        #defective = 0
        if((len(inList)-start) <= (2*num_defectives - 2)):
            end = len(inList)
            loops+=1
            for idx, val in enumerate(inList[start:end]):
                if val == 1:
                    num_defectives = num_defectives - 1
                    n = n - 1
                    defectives.append(idx+start)
                    
        else:
            #params to determine size of group
            l = n - num_defectives + 1
            alpha = int(math.floor(math.log(l/num_defectives, 2)))
            groupSize = 2**alpha
            end = start + groupSize
            group = inList[start:end]
            if any(group): 
                defective, inloops = binary_search(group)
                defective = start + defective 
                defectives.append(defective)
                num_defectives = num_defectives - 1
                start = defective + 1
                loops += inloops
            else:
                #n = n - groupSize
                start = start + groupSize

        loops += 1
        
    return len(defectives), loops

def noniidHGBSA(tree, num_defectives):
    defectives = []
    groups = h.makeList(tree)
    
    for i in range(1,len(groups)):
        if any(groups[i]):
            defectives.append(noniidHGBSA(tree[i], num_defectives))
            num_defectives = num_defectives - 1
    return defectives
