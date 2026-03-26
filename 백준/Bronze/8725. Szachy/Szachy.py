t=0
for i in range(int(input())):
    k=max(list(map(int,input().split())))
    t+=k if k>0 else 0
print(t)