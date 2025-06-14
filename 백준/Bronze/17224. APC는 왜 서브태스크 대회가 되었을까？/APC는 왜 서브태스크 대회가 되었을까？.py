n,l,k=map(int,input().split())
sub1,sub2=[],[]
pos=[]
for i in range(n):
    a,b=map(int,input().split())
    sub1.append(a)
    sub2.append(b)
for i in range(n):
    if sub2[i]<=l:
        pos.append(140)
    elif sub1[i]<=l:
        pos.append(100)
pos.sort()
print(sum(pos[-1*k:]))