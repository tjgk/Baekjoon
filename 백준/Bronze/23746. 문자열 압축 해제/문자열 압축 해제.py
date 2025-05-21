d={}
for i in range(int(input())):
    a,b=input().split()
    d[b]=a
after=input()
S,E=map(int,input().split())
before=""
for i in after:
    before+=d[i]
print(before[S-1:E])