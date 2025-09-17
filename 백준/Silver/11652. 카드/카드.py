d={}
for i in range(int(input())):
    a=int(input())
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
d=sorted(d.items(),key=lambda x:(x[1],-x[0]))
print(d[-1][0])