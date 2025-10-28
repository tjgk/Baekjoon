a=list(map(int,input().split()))
t=0
for i in a:
    if max(a)-i<=1000:
        t+=1
print(t-1)