n=int(input())
a,b=[],[]
fav,gap=0,0
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
if a==b:
    print("suspicious")
else:
    for i in range(n):
        if a.index(b[i])-i>gap:
            gap=a.index(b[i])-i
            fav=b[i]
    print(fav)