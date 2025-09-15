import sys
input=sys.stdin.readline

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0 for i in range(n-1)]
    for j in range(n-1):
        for k in range(j+1):
            if a[j+1]>=a[k]:
                b[j]+=1
    print(sum(b))