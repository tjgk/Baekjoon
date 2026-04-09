a=list(map(int,input().split()))
s=0
for i in range(5):
    s+=a[2*i]*a[2*i+1]
s//=5
b,c=map(int,input().split())
print((s*b)//c)