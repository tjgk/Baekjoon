while 1:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    sa,br=[1],[k]
    for i in range(n):
        f,r=input().split()
        f=int(f)
        if r=="SAFE":
            sa.append(f)
        else:
            br.append(f)
    if max(sa)+1==min(br):
        print(min(br),max(sa))
    else:
        print(max(sa)+1,min(br)-1)