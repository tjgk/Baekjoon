a,b,h=map(int,input().split())
i,t=0,0
while t<h:
    i+=1
    t+=a
    if t>=h:
        break
    else:
        t-=b
print(i)