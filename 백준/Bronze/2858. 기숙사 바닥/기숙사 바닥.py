r,b=map(int,input().split())
t=0
for i in range(3,(r+b)//3+1):
    for j in range(3,(r+b)//i+1):
        if t==1: break
        if i*j==b+r and (i-2)*(j-2)==b:
            print(max(i,j),min(i,j))
            t=1
            break