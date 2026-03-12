for i in range(int(input())):
    c={}
    s=1
    for j in range(int(input())):
        a,b=input().split()
        if b not in c:
            c[b]=[a]
        else:
            c[b].append(a)
    for j in c:
        s*=len(c[j])+1
    print(s-1)