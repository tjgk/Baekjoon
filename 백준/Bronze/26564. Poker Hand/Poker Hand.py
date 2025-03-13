for i in range(int(input())):
    a=list((input().split()))
    b={}
    for i in a:
        if i[0] in b:
            b[i[0]]+=1
        else:
            b[i[0]]=1
    b=sorted(b.items(),key=lambda x:x[1], reverse=True)
    print(b[0][1])
