def f(x):
    if x==0 or x==1:
        return 1
    else:
        return x*f(x-1)

while 1:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    if a+b==f(a+b)//(f(a)*f(b)):
        print(f"{a}+{b}={a+b}")
    else:
        print(f"{a}+{b}!={a+b}")