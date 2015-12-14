import pdb

with open('triangle.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    mytup = [tuple(map(int, i.split(' '))) for i in lines]

size = len(mytup) - 1

while size > 0:
    last = mytup[size]
    next_to_last = mytup[size - 1]
    replaced = []
    #pdb.set_trace()
    for i in range(len(next_to_last)):
        new = max(next_to_last[i] + last[i], next_to_last[i] + last[i+1])
        replaced.append(new)
    t = tuple(replaced)
    del mytup[-2:]
    mytup.append(t)
    size -= 1

