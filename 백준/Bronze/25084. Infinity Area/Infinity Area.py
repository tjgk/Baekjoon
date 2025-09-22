import math

for k in range(int(input())):
    r,a,b=map(int,input().split())
    s=0
    i=0
    while r!=0:
        s+=r*r*math.pi
        if i%2==0:
            r*=a
        else:
            r=int(r/b)
        i+=1
    print(f"Case #{k+1}: {s}")