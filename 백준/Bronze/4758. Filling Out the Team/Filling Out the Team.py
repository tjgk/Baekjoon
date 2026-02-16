while 1:
    a,b,c=map(float,input().split())
    if a==b==c==0:
        break
    p=0
    if a<=4.5 and b>=150 and c>=200:
        print("Wide Receiver",end=" ")
        p=1
    if a<=6 and b>=300 and c>=500:
        print("Lineman",end=" ")
        p=1
    if a<=5 and b>=200 and c>=300:
        print("Quarterback",end=" ")
        p=1
    if p==0:
        print("No positions",end=" ")
    print()