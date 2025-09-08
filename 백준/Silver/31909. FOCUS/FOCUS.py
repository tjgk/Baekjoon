n=int(input())
a=list(map(int,input().split()))
k=int(input())
p=[i for i in range(8)]

for i in a:
    t=bin(i)
    if t.count("1")==2:
        x=[]
        for i in range(len(t)):
            if t[i]=="1":
                x.append(len(t)-i-1)
        c=p.index(x[0])
        d=p.index(x[1])
        p[c],p[d]=p[d],p[c]
print(p.index(k))