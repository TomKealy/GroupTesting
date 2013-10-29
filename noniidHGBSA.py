import itertools
import math
import scipy as sp
import numpy as np
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
from collections import Counter
import random
import HuffSort as hs

def search_hufftree(items):
    defective = 0
    tree = hs.encode(items)
    l, r = hs.group(tree)

    return defective

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

def groupby_less_than_one(items):
    gb = groupby(items, lambda x: sum(x)<1)
    for k, group in gb:
        return list(group)

def HGBSA(inList, probabilities, num_defectives):

    n = len(inList)
    defectives = []
  
    start = 0    
    loops = 0
    while num_defectives > 0:

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
            group = groupby_less_than_one(probabilities)
            #end =  
            #group = inList[start:end]
            if any(group): 
                defective, inloops = search_hufftree(group)
                defective = start + defective 
                defectives.append(defective)
                num_defectives = num_defectives - 1
                start = defective + 1
                loops += inloops
            else:
                start = start + groupSize

        loops += 1
        
        return len(defectives), loops

probabilities = np.random.dirichlet([1]*1024)
probabilities = 10*probabilities
postition = random.randint(0,1024)
items = [0]*1024
items[postition] = 1
inputllsit = zip(probabilities,items)

a = HGBSA(items, probabilities, 10)
print(items)
print(probabilities)
print(a)

