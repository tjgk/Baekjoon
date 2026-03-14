for i in range(int(input())):
    a=input()
    s=0
    for j in range(len(a)//8):
        s+=1 if a[j*8:j*8+7].count("1")%2!=int(a[j*8+7]) else 0
    print(s)