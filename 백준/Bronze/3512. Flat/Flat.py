n,c=map(int,input().split())
x,y,z=0,0,0
for i in range(n):
    a,t=input().split()
    a=int(a)
    x+=a
    y+=a if t=="bedroom" else 0
    z+=a if t!="balcony" else a/2
print(x)
print(y)
print(z*c)