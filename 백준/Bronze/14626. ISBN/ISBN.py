a=input()
sum=0
for i in range(13):
    if a[i]=="*":
        pass
    elif i%2==0:
        sum+=int(a[i])
    else:
        sum+=int(a[i])*3
if a.index("*")%2==0:
        print(0 if 10-sum%10==10 else 10-sum%10)
else:
    k=0 if 10-sum%10==10 else 10-sum%10
    for i in range(10):
        if (i*3)%10==k:
            print(i)
            break