import sys
input=sys.stdin.readline
a=dict()
b=[]
n=int(input())
for i in range(n):
    t=int(input())
    if t not in a:
        a[t]=1
    else:
        a[t]+=1
    b.append(int(t))
a=dict(sorted(a.items(),key=lambda x:(-x[1],x[0])))
a=list(a.items())
b.sort()

print(round(sum(b)/n))
print(b[(n-1)//2])
if n>1:
    print(a[0][0] if a[0][1]!=a[1][1] else a[1][0])
else:
    print(b[0])
print(max(b)-min(b))