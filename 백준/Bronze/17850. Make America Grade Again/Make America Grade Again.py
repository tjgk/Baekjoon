l,h,p,e,n=map(int,input().split())
L,H,P,E=[0,0],[0,0],[0,0],[0,0]
for i in range(n):
    a,b,c=input().split()
    c1,c2=map(int,c.split("/"))
    if a=="Lab":
        L[0]+=c1
        L[1]+=c2
    elif a=="Hw":
        H[0]+=c1
        H[1]+=c2
    elif a=="Proj":
        P[0]+=c1
        P[1]+=c2
    else:
        E[0]+=c1
        E[1]+=c2
print(int(l*(L[0]/L[1])+h*(H[0]/H[1])+p*(P[0]/P[1])+e*(E[0]/E[1])))