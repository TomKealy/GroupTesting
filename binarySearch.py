#def binary_search(inList, low = 0,high = -1):
#    if not inList: return -1
#    if(high == -1): high = len(l)-1
#    #if low == high:
#      #  if inList[low] == 1: return low
#       # else: return -1
#    mid = (low + high)//2
#    upper = inList[mid:high]
#    lower = inList[0:mid-1]
#    up = sum(int(x) for x in upper)
#    lo = sum(int(x) for x in lower)
#    if up == 1: return binary_search(upper, mid, high)
#    elif lo == 1: return binary_search(lower, low, mid-1)
#    return -1

def binary_search(inList):
    low = 0
    high = len(inList) -1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        upper = inList[mid:high]
        lower = inList[low:mid]
        print(low)
        if any(lower):
            high = mid
        elif any(upper):
            low = mid
        else:
            return mid
          
        assert low < high
    return-1

def binary_splitting(inList, low=0, high=-1):
    return -1

l = [0 for x in range(256)]
l[123] = 1
bin = binary_search(l)
assert bin == 123


