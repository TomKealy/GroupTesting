with open('euler13.txt') as f:
    content = f.readlines()

sum = 0
for c in content:
    print int(c) 
    sum += int(c)

s = str(sum)
