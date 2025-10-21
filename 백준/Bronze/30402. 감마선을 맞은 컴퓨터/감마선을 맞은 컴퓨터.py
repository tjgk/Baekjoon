a=[]
p=0
while 1:
    try:
        a.append(list(input().split()))
    except:
        break
for i in a:
    if p==1:break
    for j in i:
        if j=="w":
            print("chunbae")
            p=1
            break
        elif j=="b":
            print("nabi")
            p=1
            break
        elif j=="g":
            print("yeongcheol")
            p=1
            break