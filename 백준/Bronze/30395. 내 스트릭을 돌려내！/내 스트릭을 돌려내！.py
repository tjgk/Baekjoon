n=int(input())
p=list(map(int,input().split()))
f=1
s=[0]
for i in range(n):
    if f<1:
        f+=1
    if p[i]>0:
        s[-1]+=1
    else:
        if f==1:
            f=-1
        else:
            s.append(0)
print(max(s))