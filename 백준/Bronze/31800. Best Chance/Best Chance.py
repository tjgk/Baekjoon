import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]

m1=max(a)
m2=max(a[:a.index(m1)]+a[a.index(m1)+1:])

for i in range(n):
    if a[i]==m1:
        c.append(m2-b[i])
    else:
        c.append(m1-b[i])

for i in range(n):
    print(str(a[i]-b[i]-c[i])+" ")