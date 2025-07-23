s=0
a,b=[],[]
for i in range(int(input())):
    a.append(input())
for i in range(len(a)):
    b.append(input())
for i,j in zip(a,b):
    s+=1 if i==j else 0
print(s)