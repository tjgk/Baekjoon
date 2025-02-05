for i in range(int(input())):
    p,t=map(int,input().split())
    print(max(0,p+t//4-t//7))