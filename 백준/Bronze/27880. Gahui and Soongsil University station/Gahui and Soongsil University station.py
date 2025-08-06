d=0
for i in range(4):
    h,x=input().split()
    x=int(x)
    if h=="Es":
        d+=x*21
    else:
        d+=x*17
print(d)