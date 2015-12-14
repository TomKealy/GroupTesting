with open('advent1.txt') as f:
  count = 0
  position = 0
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == '(':
        count += 1
        position += 1
    if c == ')':
        count -= 1
        position += 1
    if count == -1:
        break;

    

