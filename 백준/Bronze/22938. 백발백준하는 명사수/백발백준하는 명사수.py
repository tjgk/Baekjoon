x1,y1,r1=map(int,input().split())
x2,y2,r2=map(int,input().split())
print("YES" if ((x2-x1)**2+(y2-y1)**2)**0.5<r1+r2 else "NO")