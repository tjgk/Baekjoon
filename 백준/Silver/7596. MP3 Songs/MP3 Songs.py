t=1
while 1:
    n=int(input())
    a=[]
    if n==0:
        break
    for i in range(n):
        a.append(input())
    a.sort()
    print(t)
    for i in a:
        print(i)
    t+=1