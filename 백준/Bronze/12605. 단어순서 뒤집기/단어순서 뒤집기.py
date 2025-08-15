for i in range(int(input())):
    l=input().split()
    print(f"Case #{i+1}: ",end="")
    for i in range(len(l)):
        print(l[-1*i-1],end=" ")
    print()
    l=[]