i=int(input())
a=[]
for j in range(1,(i+1)//2):
    if i%j==0:
        a.append(j)
        a.append(i//j)
print(sum(list(set(a))))