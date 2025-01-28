for i in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if a[2]>=a[1]+a[0]:
        print(f"Case #{i+1}: invalid!")
    elif a[0]==a[2]:
        print(f"Case #{i+1}: equilateral")
    elif a[0]==a[1] or a[1]==a[2]:
        print(f"Case #{i+1}: isosceles")
    else:
        print(f"Case #{i+1}: scalene")