for i in range(int(input())):
    n,m=map(int,input().split())
    s=[[0,0] for _ in range(n)]
    r=[]
    for j in range(m):
        a,b,p,q=map(int,input().split())
        s[a-1][0]+=p
        s[a-1][1]+=q
        s[b-1][0]+=q
        s[b-1][1]+=p
    for i in s:
        if sum(i)==0:
            r.append(0)
        else:
            r.append(i[0]**2*1000/(i[0]**2+i[1]**2))
    print(int(max(r)))
    print(int(min(r)))