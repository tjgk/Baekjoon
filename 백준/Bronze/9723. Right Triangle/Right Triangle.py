for i in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if a[0]**2+a[1]**2==a[2]**2:
        print(f"Case #{i+1}: YES")
    else:
        print(f"Case #{i+1}: NO")