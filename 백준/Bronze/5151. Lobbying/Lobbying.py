for _ in range(int(input())):
    n,m,T=map(int,input().split())
    Y,N=0,0
    D=[0 for i in range(n)]
    for j in range(m):
        i,t,d=input().split()
        i,t=int(i),int(t)
        d=float(d)
        if 0<=T-t<1000:
            D[i-1]+=d
    for k in range(n):
        if input()=="Y":
            Y+=1
        else:
            N+=1/(1+(D[k]/10000))
    print(f"Data Set {_+1}:")
    print(f"{Y:.2f} {N:.2f}")
    print()