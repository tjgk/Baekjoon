h,l,a,b=map(int,input().split())
if min(2*h,l)>=min(a,b) and max(2*h,l)>=max(a,b):
    print("YES")
else:
    print("NO")