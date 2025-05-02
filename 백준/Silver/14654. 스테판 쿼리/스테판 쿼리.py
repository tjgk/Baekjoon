n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    if a[i]==1:
        if b[i]==1:
            c.append("d")
        elif b[i]==2:
            c.append("b")
        else:
            c.append("a")
    elif a[i]==2:
        if b[i]==1:
            c.append("a")
        elif b[i]==2:
            c.append("d")
        else:
            c.append("b")
    else:
        if b[i]==1:
            c.append("b")
        elif b[i]==2:
            c.append("a")
        else:
            c.append("d")
r=0
t=[c[0],1]
for i in c[1:]:
    if i=="d":
        if t[0]=="a":
            t[0]="b"
        else:
            t[0]="a"
        if r<t[1]:
            r=t[1]
        t[1]=1
    elif i==t[0]:
        t[1]+=1
    else:
        t[0]=i
        if r<t[1]:
            r=t[1]
        t[1]=1
print(max(r,t[1]))