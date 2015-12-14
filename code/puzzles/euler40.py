n, d = 1, '1'
while(len(d)<=20000000): #Increase the number to generate a 'bigger' series
    n += 1
    d += str(n)
        
print d[0]
print d[9] #Change to get value of any term
print d[99]
print d[999]
print d[9999]
print d[99999]
print d[999999]
