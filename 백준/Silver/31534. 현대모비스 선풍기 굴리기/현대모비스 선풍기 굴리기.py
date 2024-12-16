import math as m
a,b,h=map(int,input().split())
if a==b:
    print(-1)
else:
    if a>b:
        a,b=b,a
    print((((a*h/(b-a))+h)**2+b**2)*m.pi-((a*h/(b-a))**2+a**2)*m.pi)