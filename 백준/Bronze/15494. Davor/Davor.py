n=int(input())
i=0
while 1:
    i+=1
    if (n-i*1092)%364==0 and (n-i*1092)//364<=100:
        print((n-i*1092)//364)
        print(i)
        break