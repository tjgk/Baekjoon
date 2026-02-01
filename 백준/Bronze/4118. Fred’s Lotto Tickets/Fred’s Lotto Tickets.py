while 1:
    n=int(input())
    a=set()
    if n==0:
        break
    for i in range(n):
        a.update(set(list(map(int,input().split()))))
    if len(a)==49:
        print("Yes")
    else:
        print("No")