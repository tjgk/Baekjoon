for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    i=1
    while 1:
        if a[m]!=max(a):
            if m<a.index(max(a)):
                m+=len(a[a.index(max(a))+1:])
            else:
                m-=len(a[:a.index(max(a))])+1
            a=a[a.index(max(a))+1:]+a[:a.index(max(a))]
            i+=1
        else:
            print(a[:m].count(a[m])+i)
            break