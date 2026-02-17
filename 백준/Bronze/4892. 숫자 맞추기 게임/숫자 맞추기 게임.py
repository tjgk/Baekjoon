i=0
while 1:
    i+=1
    n=int(input())
    if n==0:
        break
    n*=3
    if n%2==0:
        n//=2
        print(f"{i}. even ",end="")
    else:
        n=(n+1)//2
        print(f"{i}. odd ",end="")
    print(n//3)