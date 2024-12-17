def d(a,b):
    a=int(a)
    b=int(b)
    k=[[1,2,3],[4,5,6],[7,8,9],["",0,""]]
    for i in range(4):
        for j in range(3):
            if k[i][j]==a:
                x=[i,j]
            if k[i][j]==b:
                y=[i,j]
    return abs(x[0]-y[0])+abs(x[1]-y[1])
t=input()
h=int(t[:2])
m=int(t[3:])
a=[t[:2]+t[3:]]
for i in range(4):
    if h+24*(i+1)>=100:
        break
    a.append(str(h+24*(i+1))+t[3:])
if m+60<100:
    a.append(t[:2]+str(m+60))
    for i in range(5):
        if h+(i+1)*24>=100:
            break
        a.append(str(h+24*(i+1))+str(m+60))
a.sort()
b=[]
for i in a:
    s=0
    for j in range(3):
        s+=d(i[j],i[j+1])
    b.append(s)
c=a[b.index(min(b))]
print(f"{c[:2]}:{c[2:]}")