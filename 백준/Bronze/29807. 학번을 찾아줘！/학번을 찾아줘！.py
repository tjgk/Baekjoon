n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(5-n):
    a.append(0)
if a[0]>a[2]:
    s+=abs(a[0]-a[2])*508
else:
    s+=abs(a[0]-a[2])*108
if a[1]>a[3]:
    s+=abs(a[1]-a[3])*212
else:
    s+=abs(a[1]-a[3])*305
s+=a[4]*707
print(s*4763)