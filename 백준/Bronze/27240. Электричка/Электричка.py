n,a,b=map(int,input().split())
s,t=map(int,input().split())
if s<=a and t<=a or s>=b and t>=b:
    print("Outside")
elif a+1<=s<=b-1 and a+1<=t<=b-1:
    print("City")
else:
    print("Full")