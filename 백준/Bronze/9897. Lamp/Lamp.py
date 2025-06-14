l,g,r=map(int,input().split())
t=[0 for i in range(l+1)]
dict={}
for i in range(g):
    n,a,d=input().split()
    dict[n]=[int(a),int(d)]
for i in range(r):
    a=input()
    for j in range(dict[a][0],l+1,dict[a][1]):
        if t[j]==0:
            t[j]=1
        else:
            t[j]=0
print(sum(t))