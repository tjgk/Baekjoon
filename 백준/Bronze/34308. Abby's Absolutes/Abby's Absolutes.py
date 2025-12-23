n,k=map(int,input().split())
for i in list(map(int,input().split())):
    if i<n/2+1:
        print(1,end=" ")
    else:
        print(n,end=" ")