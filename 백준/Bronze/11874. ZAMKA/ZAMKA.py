l=int(input())
d=int(input())
x=int(input())
for i in range(l,d+1):
    s=0
    for j in str(i):
        s+=int(j)
    if s==x:
        n=i
        break
for i in range(d,l-1,-1):
    s=0
    for j in str(i):
        s+=int(j)
    if s==x:
        m=i
        break
print(n)
print(m)