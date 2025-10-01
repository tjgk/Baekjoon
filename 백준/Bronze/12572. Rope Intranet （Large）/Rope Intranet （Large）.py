for i in range(int(input())):
    a=[]
    t=0
    for j in range(int(input())):
        a.append(list(map(int,input().split())))
        a.sort()
    for j in range(len(a)-1):
        for k in range(j+1,len(a)):
            if a[j][0]>a[k][0] and a[j][1]<a[k][1]:
                t+=1
            elif a[j][0]<a[k][0] and a[j][1]>a[k][1]:
                t+=1
    print(f"Case #{i+1}: {t}")