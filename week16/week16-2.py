s = "00111"
n = len(s)
for left in range(n-1):
  print('left:', left,'i<=left:有誰?',end=' ')
  for i in range(n):
    if i<=left: print(s[i], end=' ')
  print('i>left有誰?',end=' ')
  for i in range(n):
    if i>left: print(s[i],end=' ')
  print()