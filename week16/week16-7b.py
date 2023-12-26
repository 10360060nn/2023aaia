a = int(input())
s = a%60
m = a//60%60
h = a//60//60
print(F'{h:02}:{m:02}:{s:02}',end='') 