import sys
input=sys.stdin.readline
print=sys.stdout.write
b=[i*i%2010 for i in range(2010)]

n=int(input())
a=list(map(int,input().split()))
for i in range(int(input())):
    k,l,r=map(int,input().split())
    if k==1:
        for j in range(l-1,r):
            a[j]=b[a[j]]
    if k==2:
        print(str(sum(a[l-1:r]))+'\n')