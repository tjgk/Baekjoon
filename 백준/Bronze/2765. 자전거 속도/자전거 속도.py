i=0
while 1:
    i+=1
    r2,s,t=map(float,input().split())
    d=s*r2*3.1415927/(12*5280)
    if s==0:
        break
    print(f"Trip #{i}: {d:.2f} {3600*d/t:.2f}")