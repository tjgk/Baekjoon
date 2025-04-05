n,m=map(int,input().split())
a=[]
t=[-1,1]
for i in range(m):
    a.append(list(map(int,input().split())))
r,c=0,0
for i in a:
    for j in t:
        if [i[0]+j,i[1],i[2]] in a:
            c+=1
    for j in t:
        if [i[0],i[1]+j,i[2]] in a:
            c+=1
    for j in t:
        if [i[0],i[1],i[2]+j] in a:
            c+=1
    if c==6:
        r+=1
    c=0
print(r)