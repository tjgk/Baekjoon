import sys
input=sys.stdin.readline

m,n=map(int,input().split())
dir=0
x,y=0,0
tf=0
for i in range(n):
    a,b=input().split()
    if a=="TURN":
        if b=="0":
            dir+=90
        else:
            dir-=90
        if dir<0:
            dir+=360
        elif dir>=360:
            dir-=360
    else:
        if dir==0:
            x+=int(b)
        elif dir==90:
            y+=int(b)
        elif dir==180:
            x-=int(b)
        else:
            y-=int(b)
    if x<0 or x>m or y<0 or y>m:
        tf=1
        print(-1)
        break
if tf==0:
    print(x,y)