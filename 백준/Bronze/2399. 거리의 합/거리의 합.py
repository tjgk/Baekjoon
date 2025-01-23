n=int(input())
a=list(map(int,input().split()))
s=0
a.sort()
for i in range(n):
    s+=a[i]*(1-n+i*2)
print(s*2)