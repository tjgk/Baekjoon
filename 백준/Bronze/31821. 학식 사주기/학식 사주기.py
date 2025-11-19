a=[]
s=0
for i in range(int(input())):
    a.append(int(input()))
for i in range(int(input())):
    s+=a[int(input())-1]
print(s)