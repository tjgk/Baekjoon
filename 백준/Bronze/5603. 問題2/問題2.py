n=int(input())
a=input()
for i in range(n):
    t=[1,a[0]]
    b=""
    k=0
    for j in a[1:]:
        k+=1
        if j!=t[1]:
            b+=str(t[0])+str(t[1])
            t[0]=1
            t[1]=j
            if k==len(a)-1:
                b+=str(t[0])+j
        else:
            t[0]+=1
            if k==len(a)-1:
                b+=str(t[0])+j
    a=b
print(a)