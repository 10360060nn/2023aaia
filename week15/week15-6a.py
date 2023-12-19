a,b,c,d = list(map(int,input().split()))
ans = (a-c)*(b-d)
if ans<0 : ans=(-1)*ans
print(ans,end='')