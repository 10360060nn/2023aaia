a = list(map(int,input().split()))

sum = 0
for i in a:
	sum=sum+i
	if i<0 :      #if i>0: sum=sum+i
		sum=sum+(-(i))
print(sum,end='')