l,p=map(int,input().split())
t=0
r=0
for i in range(p):
    a,b=input().split()
    b=int(b)
    if a=="enter":
        if t+b<=l:
            t+=b
        else:
            r+=1
    else:
        t-=b
print(r)