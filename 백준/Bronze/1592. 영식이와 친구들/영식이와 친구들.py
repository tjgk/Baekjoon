n,m,l=map(int,input().split())
t=[0 for i in range(n+1)]
t[1]+=1
i=0
p=1
while m not in t:
    if t[p]%2==1:
        if p+l<=n:
            p+=l
        else:
            p=p+l-n
    else:
        if p-l>=1:
            p-=l
        else:
            p=p-l+n
    t[p]+=1
    i+=1
print(i)