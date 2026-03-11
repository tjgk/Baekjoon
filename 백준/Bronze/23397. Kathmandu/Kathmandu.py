t,d,m=map(int,input().split())
a,b=[],[]
for i in range(m):
    a.append(int(input()))
if m==0 and t<=d:
    print("Y")
elif t>d:
    print("N")
else:
    if a[0]!=0:
        a=[0]+a[:]
    if a[-1]!=d:
        a.append(d)
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    print("Y" if max(b)>=t else "N")