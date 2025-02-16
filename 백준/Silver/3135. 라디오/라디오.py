a,b=map(int,input().split())
s=abs(b-a)
for i in range(int(input())):
    t=int(input())
    if abs(t-b)<s:
        s=abs(t-b)+1
print(s)