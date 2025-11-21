n=int(input())
k=input()
t=0
for i in k:
    if int(i)%2==0:
        t+=1
if t>n/2:
    print(0)
elif t<n/2:
    print(1)
else:
    print(-1)