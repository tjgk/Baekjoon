a=list(map(int,input().split()))
a.sort()
d={"A":a[0],"B":a[1],"C":a[2]}
t=input()
for i in t:
    print(d[i],end=" ")