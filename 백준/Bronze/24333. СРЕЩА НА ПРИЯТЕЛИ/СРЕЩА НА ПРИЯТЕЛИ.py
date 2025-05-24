l1,r1,l2,r2,k=map(int,input().split())
t=[0 for i in range(50001)]
for i in range(l1,r1+1):
    t[i]+=1
for i in range(l2,r2+1):
    t[i]+=1
t[k]-=1
print(t.count(2))