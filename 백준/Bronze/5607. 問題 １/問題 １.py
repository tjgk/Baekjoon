x,y=0,0
for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        x+=a+b
    elif a<b:
        y+=a+b
    else:
        x+=a
        y+=b
print(x,y)