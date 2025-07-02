n=int(input())
s=list(map(int,input().split()))
c=int(input())
t=0
for i in s:
    t+=i//c
    t+=1 if i%c!=0 else 0
print(t*c)