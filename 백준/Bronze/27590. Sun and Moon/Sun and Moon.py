ds,ys=map(int,input().split())
dm,ym=map(int,input().split())
s,m=ds,dm
i=0
while s!=0 or m!=0:
    i+=1
    s+=1
    m+=1
    if s==ys:
        s=0
    if m==ym:
        m=0
print(i)