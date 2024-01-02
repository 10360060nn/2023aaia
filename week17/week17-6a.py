a = input()
n = len(a)
for i in range(n):
	if (n-i)%3==0 and i!=0:
		print(',',end='')
	print(a[i],end='')