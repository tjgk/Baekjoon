a=[]
b=[0,1,3,3,5,9]
c=["K","P","N","B","R","Q"]
d=["k","p","n","b","r","q"]
for i in range(8):
    a.append(input())
s=0
for i in a:
    for j in i:
        if j in c:
            s+=b[c.index(j)]
        elif j in d:
            s-=b[d.index(j)]
print(s)