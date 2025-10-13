n,k=map(int,input().split())
b,c=0,0
for i in range(n):
    m=input()
    if m=="save":
        c=b
    elif m=="load":
        b=c
    elif m=="shoot":
        b-=1
    else:
        b+=k
    print(b)