import sys

input=sys.stdin.readline
print=sys.stdout.write

def f(x):
    t=1
    for i in range(x):
        t*=(i+1)
    return t

while 1:
    n=input().strip()
    s=0
    if n=="0":
        break
    for i in range(len(n)):
        s+=int(n[i])*f(len(n)-i)
    print(str(s)+"\n")