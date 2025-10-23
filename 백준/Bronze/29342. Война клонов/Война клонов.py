n=int(input())
x,y=0,0
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        x+=1
    else:
        y+=1
print(x*y)