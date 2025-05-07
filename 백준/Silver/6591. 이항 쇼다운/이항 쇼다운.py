import sys
input=sys.stdin.readline
print=sys.stdout.write

def f(x):
    if x==0 or x==1:
        return 1
    else:
        return f(x-1)*x

while 1:
    n,k=map(int,input().split())
    k=min(k,n-k)
    r=1
    if n+k==0:
        break
    else:
        for i in range(k):
            r*=n-i
    print(str(r//f(k))+"\n")