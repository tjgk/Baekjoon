a=[]
for i in range(9):
    a.append(list(map(int,input().split())))
M=[0,1,1]
for i in range(9):
    for j in range(9):
        if a[i][j]>M[0]:
            M=[a[i][j],i+1,j+1]
print(M[0])
print(M[1],M[2])