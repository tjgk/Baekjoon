for i in range(int(input())):
    n=bin(int(input()))[2:]
    for j in range(len(n)):
        if n[-1*(j+1)]=="1":
            print(j,end=" ")
    print()