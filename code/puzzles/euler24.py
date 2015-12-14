def next_lexigraphic_permutation(L):
    
    n = len(L)

    #Find the largest i s.t. L[i] < L[i+1] (no such i => L is last perm)
    i = n -2
    while L[i] < L[i+1]:
        i -= 1
    
    if i < 0:
        return False

    #Find the largest j s.t. L[i] < L[j]
    
    j = n - 1
    while L[i] < L[j]:
        j -= 1

    #Swap L[i], L[i]
    L[i], L[j] = L[j], L[i]
    
    #Reverse L[i+1 ... n]
    r = n - 1
    s = i+1
    while r>s:
        L[r] , L[s]  = L[s], L[r]
        r -= 1
        s += 1
    return True

array  = [0,1,2,4,3]
while next_lexigraphic_permutation(array):
    print array
