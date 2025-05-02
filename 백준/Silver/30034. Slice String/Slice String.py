n=int(input())
A=list(input().split())
m=int(input())
B=list(input().split())
k=int(input())
c=list(input().split())
s=int(input())
l=input()
a,b=[],[]
for i in A:
    if i not in c:
        a.append(i)
for i in B:
    if i not in c:
        b.append(i)
ab=a+b+[" "]
t=1
for i in range(len(l)):
    if l[i] in ab:
        if t==0 and i!=len(l)-1:
            print()
            t=1
        else:
            pass
    else:
        print(l[i],end="")
        t=0