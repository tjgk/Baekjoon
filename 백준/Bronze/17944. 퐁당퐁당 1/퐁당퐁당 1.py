n,t=map(int,input().split())
k=[0,0]
for i in range(t%(4*n-2)):
    if i+1<=2*n:
        k[0]+=1
    else:
        k[1]+=1
print(2 if t%(4*n-2)==0 else k[0]-k[1])