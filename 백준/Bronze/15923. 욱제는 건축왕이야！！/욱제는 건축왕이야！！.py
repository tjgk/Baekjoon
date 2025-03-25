l=0
a=[]
for i in range(int(input())):
    a.append(list(map(int,input().split())))
a.append(a[0])
for i in range(len(a)-1):
    if a[i][0]==a[i+1][0]:
        l+=abs(a[i+1][1]-a[i][1])
    else:
        l+=abs(a[i+1][0]-a[i][0])
print(l)