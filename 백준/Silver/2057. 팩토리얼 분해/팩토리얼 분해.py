def f(x):
    if x==0 or x==1:
        return 1
    else:
        return x*f(x-1)
n=int(input())
p=0
if n==0:
    print("NO")
else:
    for i in range(20,-1,-1):
        if n==0:
            print("YES")
            p=1
            break
        elif f(i)<=n:
            n-=f(i)
    if p==0 and n==0:
        print("YES")
    elif p==0:
        print("NO")