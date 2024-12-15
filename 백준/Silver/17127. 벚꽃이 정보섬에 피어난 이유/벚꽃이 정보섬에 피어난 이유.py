def m(x):
    t=1
    for i in x:
        t*=i
    return t
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            b.append(m(a[:i+1])+m(a[i+1:j+1])+m(a[j+1:k+1])+m(a[k+1:]))
print(max(b))