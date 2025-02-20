while 1:
    try:
        n,b,m=map(float,input().split())
        i=0
        while n<m:
            i+=1
            n*=(1+b/100)
        print(i)
    except:
        break