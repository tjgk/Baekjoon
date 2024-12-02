pt,p1,p2=map(float,input().split())
pt=round(pt*100)
p1=round(p1*100)
p2=round(p2*100)
x,i=0,1
if pt%p2==0:
    print(0,pt//p2)
    x=1
while i*p1<=pt:
    if (pt-(p1*i))%p2==0:
        print(i,(pt-i*p1)//p2)
        x=1
    i+=1
if x==0:
    print("none")