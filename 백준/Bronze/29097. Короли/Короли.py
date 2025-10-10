n,m,k,a,b,c=map(int,input().split())
d={"Joffrey":a*n,"Robb":b*m,"Stannis":c*k}
l=sorted(d.items(),key=lambda x:x[1])
for i in l:
    if i[1]==max(l,key=lambda x:x[1])[1]:
        print(i[0],end=" ")