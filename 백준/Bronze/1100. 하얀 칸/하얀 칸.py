a=[]
for i in range(8):
    a.append(input())
c=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if a[i][j]=="F":
                c+=1
print(c)