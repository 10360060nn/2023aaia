a = [1,1]
for i in range(2,100):
  a.append(a[i-1]+a[i-2])   #append() 方法用于在列表末尾添加新的对象。
print(a)