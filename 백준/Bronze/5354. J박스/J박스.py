for i in range(int(input())):
    n=int(input())
    for j in range(n):
        if j==0:
            print("#"*n)
        elif j==n-1:
            print("#"*n)
        else:
            print(f"#{"J"*(n-2)}#")
    print()