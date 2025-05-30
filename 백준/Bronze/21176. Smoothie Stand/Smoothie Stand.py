import sys
input=sys.stdin.readline

k,r=map(int,input().split())
a=list(map(int,input().split()))
ans=[]

for i in range(r):
    b=list(map(int,input().split()))
    c=[]
    for j in range(k):
        if b[j]==0:
            pass
        else:
            c.append(a[j]//b[j])
    ans.append(min(c)*b[-1])

print(max(ans))