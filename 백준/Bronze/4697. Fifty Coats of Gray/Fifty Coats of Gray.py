while 1:
    n,w,l,h,a,m=map(int,input().split())
    if n==0:
        break
    s=w*l+w*h*2+l*h*2
    for i in range(m):
        x,y=map(int,input().split())
        s-=x*y
    print(s*n//a if int(s*n/a)==s*n/a else s*n//a+1)