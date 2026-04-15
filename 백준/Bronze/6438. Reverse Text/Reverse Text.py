for i in range(int(input())):
    a=input()
    for j in range(len(a)):
        print(a[-1*(j+1)],end="")
    print()