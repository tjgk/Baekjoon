a,b=map(int,input().split())
a="0"*(10-len(bin(a)[2:]))+bin(a)[2:]
b="0"*(10-len(bin(b)[2:]))+bin(b)[2:]
c=""
for i,j in zip(a,b):
    c+="1" if i!=j else "0"
print(int(c,2))