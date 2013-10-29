# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:19:12 2013

@author: tk12098
"""
from GroupTesting import HGBSA, noniidHGBSA
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
from collections import Counter
from pylab import *
import huffman0 as h

tests = []
numtests = 100
for i in range(0, numtests):
    #random
    zeros = [0] * 1024
    ones = [1] * 10
    #ones = [randint(0,1023) for _ in range(0,10)]
    l =  zeros + ones
    shuffle(l)
    where_the_ones_are = [i for i, x in enumerate(l) if x == 1] 
    #print(where_the_ones_are)
    #assert HGBSA(l, 10) == where_the_ones_are
    tests.append(HGBSA(l,10))

count = [x[0] for x in tests]
found = [x[1] for x in tests]
found.sort()
num = Counter(found)
freqs = [x for x in num.values()]
cumsum = [sum(item for item in freqs[0:rank+1]) for rank in range(len(freqs))]
normcumsum  = [float(x)/numtests for x in cumsum]

print(freqs)
print(cumsum)
print(normcumsum)
print(sorted(num.keys()))


#with open('results.csv', "wb") as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(sorted(num.keys()))
#    wr.writerow(normcumsum)
#
figure(0)
plt.plot(sorted(num.keys()), normcumsum)
plt.xlim(0,100)
plt.show()



#tests = []
#for i in range(0, 100):
#    print('in here')
#    inlist = [0]*1024
#    ones = [i for i in range(1,1024,30)]
#    for val in ones:
#        inlist[val] = 1
#    l =  inlist + ones
#    shuffle(l)
#    where_the_ones_are = [i for i, x in enumerate(l) if x == 1] 
#    tests.append(HGBSA(l,35))
#
##print(tests)
#
#count = [x[0] for x in tests]
#found = [x[1] for x in tests]
#found.sort()
#num = Counter(found)
#freqs = [x for x in num.values()]
#cumsum = [sum(item for item in freqs[0:rank+1]) for rank in range(len(freqs))]
#normcumsum  = [float(x)/numtests for x in cumsum]
#print(cumsum)
#print(normcumsum)
#print(num.keys())
#print(len(normcumsum))
#print(len(num.keys()))
#
#plt.plot(num.keys(), normcumsum)
#plt.xlim(0,500)
#plt.show()

#tests = []
#numtests = 10
#for i in range(0, numtests):
#    #random
#    zeros = [0] * 100
#    ones = [1] * 1
#    l =  zeros + ones
#    shuffle(l)
#    where_the_ones_are = [i for i, x in enumerate(l) if x == 1] 
#    probs = np.random.dirichlet([1]*1024).tolist()
#   tree = h.makeHuffmanTree(zip(probs, l))
#    tests.append(noniidHGBSA(tree,1))

#print(tests)
#count = [x[0] for x in tests]
#found = [x[1] for x in tests]
#found.sort()
#num = Counter(found)
#freqs = [x for x in num.values()]
#nums = [x for x in num.keys()]
#print(freqs)
#cumsum = [sum(item for item in freqs[0:rank+1]) for rank in range(len(freqs))]
#normcumsum  = [float(x)/numtests for x in cumsum]
#print(cumsum)
#print(normcumsum)
#print(sorted)
#
#figure(1)
#plt.plot(num.keys(), normcumsum)
#plt.xlim(0,150)
#plt.show()
