import HuffSort as hs
import huffman0 as hz

def search_hufftree(tree):
    defective = 0
    l, r = hs.group(tree)
    if any(l):
        search_hufftree(l)
    else:
        search_hufftree(r)
    return defective

exampleData = [(0,0.5), (0,.25), (1,0.125), (0,0.125)]
#exampleData = {'0':0.5,'0':0.25, '1':0.125, '0':0.125}
huffTree = hz.makeHuffmanTree(exampleData)
groups = hz.leaves(huffTree)

