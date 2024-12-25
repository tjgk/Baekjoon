a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=(a[0]+a[1]+a[2]+a[3])/2
B=(b[0]+b[1]+b[2]+b[3])/2
if A>B:
    print("Gunnar")
elif A<B:
    print("Emma")
else:
    print("Tie")