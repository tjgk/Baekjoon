n=int(input())
a=n
t=0
if n==1:
    print(1,0)
else:
    while n%2==0:
        n//=2
        t+=1
    print(a//(2**t),t)