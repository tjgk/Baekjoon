a,b,c,d=map(int,input().split())
p,m,n=map(int,input().split())
r=[0 for i in range(max([p,m,n])+1)]
for i in range(1,len(r)):
    if i%(a+b)<=a and i%(a+b)!=0:
        r[i]+=1
    if i%(c+d)<=c and i%(c+d)!=0:
        r[i]+=1
for i in [p,m,n]:
    print(r[i])