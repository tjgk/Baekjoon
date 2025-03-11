n,A=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i//A
print(s)