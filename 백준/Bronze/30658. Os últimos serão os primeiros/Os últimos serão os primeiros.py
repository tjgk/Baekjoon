while 1:
    a=[]
    n=int(input())
    if n==0: break
    for i in range(n):
        a.append(int(input()))
    for i in a[::-1]:
        print(i)
    print(0)