while 1:    
    n=int(input())
    k=0
    x=0
    if n==-1:
        break
    for i in range(n):
        s,t=map(int,input().split())
        x+=s*(t-k)
        k=t
    print(x,"miles")