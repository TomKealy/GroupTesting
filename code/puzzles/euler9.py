import pdb

def triple(a,b,c):
    "Checks if (a,b,c) is a Pythag Triple"
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def triples():
    "construct a list of pythagorean triples"
    triples = []
    for n in xrange(1,26):
        for m in xrange(1,n):
            a = n**2 - m**2
            b = 2*m*n
            c = n**2 + m**2
            if a > 0 and b > 0 and c > 0:
                if triple(a,b,c):
                    triples.append((a,b,c))
    return triples

triples = triples()

for triple in triples:
    if sum(triple) == 1000:
        print triple[0]*triple[1]*triple[2]
