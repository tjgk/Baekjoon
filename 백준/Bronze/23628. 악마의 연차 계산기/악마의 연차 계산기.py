S=list(map(int,input().split()))
E=list(map(int,input().split()))
y,m,days=0,0,0
days=(E[0]*360+E[1]*30+E[2])-(S[0]*360+S[1]*30+S[2])
m=min(36,days//30)
if (days//360)%2==1:
    A=(days//720)*(days//720-1)+(days//720)
else:
    A=(days//720)*(days//720-1)
y=15*(days//360)+A
print(y,m)
print(f"{days}days")