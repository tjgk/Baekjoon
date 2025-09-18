import sys
sys.stdin.readline

for i in range(int(input())):
    a,m=[],0
    for j in range(int(input())):
        a.append(int(input()))
    t=len(a)
    while 1:
        b=[]
        for j in a:
            b.append(j%t)
        if len(b)==len(list(set(b))):
            print(t)
            break
        else:
            t+=1