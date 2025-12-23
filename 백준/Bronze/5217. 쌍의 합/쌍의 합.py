for i in range(int(input())):
    n=int(input())
    t=0
    print(f"Pairs for {n}: ",end="")
    for i in range(1,n):
        for j in range(i+1,n):
            if i+j==n:
                if t==1:
                    print(",",end=" ")
                print(i,j,end="")
                t=1
    print()