t=[0 for _ in range(720)]
n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    s=a*60+b-540
    e=c*60+d-540
    for i in range(s,e+1):
        t[i]+=1
z=[]
for i in range(720):
    if t[i]==n:
        z.append(i)
if len(z)>1:
    print("TAIP")
    print(z[0]//60+9,z[0]%60,z[-1]//60+9,z[-1]%60)
else:
    print("NE")