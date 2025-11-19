import sys
print=sys.stdout.write
n,m=map(int,input().split())
t=0
for i in range(n):
    for j in range(m):
        t+=1
        print(str(t))
        if j!=m-1:
            print(" ")
    print("\n")