def f(x):
    global a,n
    for i in str(x):
        if i not in a:
            a.append(i)
while 1:
    try:
        n=int(input())
        a=[]
        k=0
        while 1:
            k+=1
            f(k*n)
            if len(a)==10:
                print(k)
                break
    except:
        break