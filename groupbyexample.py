from itertools import groupby

def groupby_even_odd(items):
    f = lambda x: 'eve' if x%2 == 0 else 'odd'
    gb = groupby(sorted(items,key=f), f)
    for k, items in gb: 
        print '%s: %s' % (k, ','.join(map(str, items)))

def groupby_less_than_one(items):
    gb = groupby(items, lambda x: sum(x)<1)
    for k, group in gb:
        return list(group)

