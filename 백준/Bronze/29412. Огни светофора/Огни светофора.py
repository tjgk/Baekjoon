g,gb,y,r,ry=map(int,input().split())
t=int(input())
c=[]
for i in range(g):
    c.append("g")
for i in range(gb):
    c.append("gb")
for i in range(y):
    c.append("y")
for i in range(r):
    c.append("r")
for i in range(ry):
    c.append("ry")
red,yellow,green=(t//len(c))*(r+ry),(t//len(c))*(y+ry),(t//len(c))*(g+gb//2)
for i in range(t%len(c)):
    if c[i]=="g":
        green+=1
    elif c[i]=="gb":
        green+=0.5
    elif c[i]=="y":
        yellow+=1
    elif c[i]=="r":
        red+=1
    else:
        yellow+=1
        red+=1
print(red,yellow,int(green))