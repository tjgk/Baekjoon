a=input()
b=[]
for i in a:
    b.append(i)
b.sort()
p,r=b[0],b[0]
for i in b[1:]:
    if i!=p:
        r+=i
        p=i
print(len(b)-len(r))