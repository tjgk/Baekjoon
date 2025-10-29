x=int(input())
t=0
for i in range(int(str(x)[:2]),100):
    if t==1: break
    for j in range(int(str(x)[2:]) if i==int(str(x)[:2]) else 0,100):
        if (i+j)**2==i*100+j and x!=i*100+j:
            print(i*100+j)
            t=1
            break
    if i==99:
        print(-1)
        break