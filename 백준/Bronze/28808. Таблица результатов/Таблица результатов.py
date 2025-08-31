n,m=map(int,input().split())
t=0
for i in range(n):
    a=input()
    if a.count("+")>=1:
        t+=1
print(t)