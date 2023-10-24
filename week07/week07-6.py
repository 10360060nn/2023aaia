s = "abcdabcd"
d = {}
for c in s:
  if c in d:               #若已經在陣列裡面
    d[c] = d[c] + 1
  else:                   #若是是第一次出現
    d[c] = 1
  print('現在讀到的字典',c,"字典變成",d)