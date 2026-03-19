n=int(input())
a=list(input().split())
t=1
for i in a:
    try:
        print(i[t-1],end="")
        t=len(i)
    except:
        print(" ",end="")
        t=len(i)