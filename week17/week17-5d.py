a = list(map(int,input().split()))
sum=0
for i in a:
	if i%3==0:
		sum=sum+1
print(sum)