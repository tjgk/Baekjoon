a=list(map(int,input().split()))
b=[]
for i in range(9):
    for j in range(i+1,10):
        b.append(a[i]|a[j])
for i in range(8):
    for j in range(i+1,9):
        for k in range(j+1,10):
            b.append(a[i]|a[j]|a[k])
r=b[0]
for i in range(len(b)-1):
    r=r^b[i+1]
print(r)