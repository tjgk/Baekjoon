m=200
for i in range(int(input())):
    a,b=map(int,input().split())
    if a+b<=m:
        m=a+b
print(m)