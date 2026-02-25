import sys
input=sys.stdin.readline
print=sys.stdout.write

tar=[]
ans=[]
tmp=[]
p=0
c=1

for i in range(int(input())):
    tar.append(int(input()))

for i in tar:
    while c<=i:
        tmp.append(c)
        ans.append("+")
        c+=1
    if tmp[-1]==i:
        tmp.pop()
        ans.append("-")
    else:
        print("NO")
        p=1
        break
if p==0:
    for i in ans:
        print(i+"\n")
