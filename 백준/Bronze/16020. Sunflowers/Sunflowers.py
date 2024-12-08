n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

def out(a):
    for i in a:
        for j in i:
            print(j,end=" ")
        print("")

if a[n-1][n-1]==max(max(a)):
    out(a)
elif a[n-1][0]==max(max(a)):
    b=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            b[n-1-j][i]=a[i][j]
    out(b)
elif a[0][0]==max(max(a)):
    c=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[n-1-i][n-1-j]=a[i][j]
    out(c)
else:
    d=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            d[j][n-1-i]=a[i][j]
    out(d)