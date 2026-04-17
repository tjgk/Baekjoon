a=[]
while 1:
    try:
        b=list(map(int,input().split()))
        for i in b:
            a.append(i)
    except:
        break
for i in a[:-1]:
    if i==1:
        print(i,"DEFICIENT")
        continue
    s=set()
    s.add(1)
    for j in range(2,i//2+1):
        if i%j==0:
            s.add(j)
            s.add(i//j)
    if sum(list(s))>i:
        print(i,"ABUNDANT")
    elif sum(list(s))<i:
        print(i,"DEFICIENT")
    else:
        print(i,"PERFECT")