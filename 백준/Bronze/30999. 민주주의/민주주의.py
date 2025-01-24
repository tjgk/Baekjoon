n,m=map(int,input().split())
s=0
for i in range(n):
    if input().count("O")>m/2:
        s+=1
print(s)