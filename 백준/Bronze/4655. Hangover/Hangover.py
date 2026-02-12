while 1:
    n=float(input())
    if n==0:
        break
    i=1
    s=0
    while 1:
        i+=1
        if s+1/i<n:
            s+=1/i
        else:
            break
    print(i-1,"card(s)")