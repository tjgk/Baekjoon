a,b,h,w=map(int,input().split())
if h%a==0:
    if w%b==0:
        print((h//a)*(w//b))
    else:
        print((h//a)*(w//b+1))
else:
    if w%b==0:
        print((h//a+1)*(w//b))
    else:
        print((h//a+1)*(w//b+1))