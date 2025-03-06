n=int(input())
z=[]
for i in range(n):
    z.append(int(input()))
z.sort()
g=0
for i in z:
    g+=1
    if g>=i+1:
        print(g)
        break