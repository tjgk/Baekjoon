w,o,d=0,0,-30
for i in range(int(input())):
    a=list(input().split())
    if a[0]=="temperature":
        d+=int(a[1][1:])
    elif a[0]=="oxygen":
        o+=int(a[1][1:])
    else:
        w+=int(a[1][1:])
print("liveable" if w>=9 and o>=14 and d>=8 else "not liveable")