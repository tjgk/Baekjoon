n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if len(a)>len(b):
    for i in range(len(a)-len(b)):
        b.append(0)
elif len(a)<len(b):
    for i in range(len(b)-len(a)):
        a.append(0)
s=0
for i in range(len(a)):
    if b[i]-a[i]>s:
        s=b[i]-a[i]
print(s)