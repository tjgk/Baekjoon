n,m=map(int,input().split())
x,y="",""
for i in range(n):
    for j in input():
        x+=j*2
    x+=" "
for i in range(n):
    y+=input()+" "
print("Eyfa" if x==y else "Not Eyfa")