import math

n=int(input())
a=list(map(int,input().split()))
b=[0 for i in range(63)]
for i in a:
    if i!=0:
        b[int(math.log(i,2))]+=1
for i in range(62):
    if b[i]//2>=1:
        b[i+1]+=b[i]//2
        b[i]=0
for i in range(62,-1,-1):
    if b[i]!=0:
        print(2**i)
        break