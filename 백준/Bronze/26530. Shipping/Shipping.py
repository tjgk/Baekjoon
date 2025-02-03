for i in range(int(input())):
    s=0
    for j in range(int(input())):
        a=list(input().split())
        s+=float(a[1])*float(a[2])
    print(f"${s:.2f}")