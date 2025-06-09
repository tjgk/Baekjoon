r=[1001,1001]
for i in range(int(input())):
    x,y=map(int,input().split())
    if y<r[1]:
        r=[x,y]
print(r[0],r[1])