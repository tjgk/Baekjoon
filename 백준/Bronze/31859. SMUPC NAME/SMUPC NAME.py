n,s=input().split()
n=int(n)
a=[]
r=0
for i in s:
    if i not in a:
        a.append(i)
    else:
        r+=1
a.append(str(r+4))
a=[str(1906+n)]+a
a="".join(a)
print("smupc_"+"".join(reversed(a)))