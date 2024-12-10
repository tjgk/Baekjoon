n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
S=sum(a)
s=0
for i in range(n):
    s+=a[i]*b[i]
print(S)
print(S-s)