a=[]
while 1:
    try:
        a.append(list(input().split()))
    except:
        print(len(a))
        break