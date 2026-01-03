t=0
m=list(map(int,input().split()))
for i in range(int(input())):
    b,l,s=map(float,input().split())
    if l>=2 and s>=17:
        t+=m[int(b)]
print(t)