k=int(input())
a=[[1,0]]
for i in range(45):
    a.append([a[-1][1],a[-1][0]+a[-1][1]])
print(a[k][0],a[k][1])