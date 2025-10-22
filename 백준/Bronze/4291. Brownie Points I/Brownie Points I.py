while 1:
    n=int(input())
    if n==0:
        break
    a=[]
    s,o=0,0
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in a:
        if i[0]>a[n//2][0]:
            if i[1]>a[n//2][1]:
                s+=1
            elif i[1]<a[n//2][1]:
                o+=1
        elif i[0]<a[n//2][0]:
            if i[1]>a[n//2][1]:
                o+=1
            elif i[1]<a[n//2][1]:
                s+=1
    print(s,o)