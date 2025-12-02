n=int(input())
a=list(map(int,input().split()))
s,t=0,0
for i in a:
    if i==0:
        t-=1
        s+=t
    else:
        t+=1
        s+=t
print(s)