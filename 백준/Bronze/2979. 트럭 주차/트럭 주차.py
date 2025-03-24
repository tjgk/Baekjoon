a,b,c=map(int,input().split())
p=[0 for i in range(101)]
for i in range(3):
    s,e=map(int,input().split())
    for j in range(s,e):
        p[j]+=1
print(p.count(3)*c*3+p.count(2)*b*2+p.count(1)*a)