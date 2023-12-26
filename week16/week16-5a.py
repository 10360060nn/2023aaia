a = int(input())
i=1
while a>0:
	now = a%10
	print(now*i, end=' ')
	a = a//10
	i=i*10