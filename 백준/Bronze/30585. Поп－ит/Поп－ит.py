r,c=map(int,input().split())
a=[]
for i in range(r):
    a.append(input())
x,y=0,0
for i in a:
    for j in i:
        if j=="0":
            x+=1
        else:
            y+=1
print(min(x,y))