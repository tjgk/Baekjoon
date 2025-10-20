n,h=map(int,input().split())
a=list(map(int,input().split()))
t=0
for i in a:
    if h>=i:
        t+=1
print(t)