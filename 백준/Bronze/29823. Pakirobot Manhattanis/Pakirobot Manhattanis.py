n=int(input())
a=input()
x,y=0,0
for i in a:
    if i=="N":
        y+=1
    elif i=="S":
        y-=1
    elif i=="E":
        x+=1
    else:
        x-=1
print(abs(x)+abs(y))