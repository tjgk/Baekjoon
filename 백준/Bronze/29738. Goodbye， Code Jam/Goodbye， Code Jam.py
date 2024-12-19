for i in range(int(input())):
    a=int(input())
    if a<=25:
        print(f"Case #{i+1}: World Finals")
    elif a<=1000:
        print(f"Case #{i+1}: Round 3")
    elif a<=4500:
        print(f"Case #{i+1}: Round 2")
    else:
        print(f"Case #{i+1}: Round 1")