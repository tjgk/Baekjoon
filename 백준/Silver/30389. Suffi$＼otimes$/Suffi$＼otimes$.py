r=dict()
for i in range(int(input())):
    a=input()
    for j in range(len(a)):
        if a[j:] in r:
            r[a[j:]]+=1
        else:
            r[a[j:]]=1
c=0
for i in r.values():
    if i%2==1:
        c+=1
print(c)