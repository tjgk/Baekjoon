M=0
a=[0,0,0]
for i in range(int(input())):
    t,s=map(int,input().split())
    if s>M:
        M=s
        a=[t,s,i]
if a[1]==0:
    print(0)
else:
    print(a[0]+a[2]*20)