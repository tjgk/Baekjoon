c=0
for i in range(int(input())):
    l,w,d,g=map(float,input().split())
    if ((l<=56 and w<=45 and d<=25) or l+w+d<=125) and g<=7:
        c+=1
        print(1)
    else:
        print(0)
print(c)