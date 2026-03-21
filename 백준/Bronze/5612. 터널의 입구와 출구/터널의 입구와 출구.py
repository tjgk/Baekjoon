n=int(input())
m=int(input())
M=m
p=0
for i in range(n):
    a,b=map(int,input().split())
    m+=a-b
    if M<m:
        M=m
    if m<0:
        print(0)
        p=1
        break
if p==0:
    print(M)