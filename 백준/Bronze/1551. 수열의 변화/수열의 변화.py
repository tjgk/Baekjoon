n,k=map(int,input().split())
a=list(map(int,input().split(",")))
b=[]
for j in range(k):
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    a=b[:]
    b=[]
print(",".join(map(str,a)))