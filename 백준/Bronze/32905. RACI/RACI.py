n,m=map(int,input().split())
tf=1
for i in range(n):
    a=list(input().split())
    if a.count("A")!=1:
        tf=0
print("Yes" if tf==1 else "No")