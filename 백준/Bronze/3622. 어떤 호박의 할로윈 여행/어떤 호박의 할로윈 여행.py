A,a,B,b,P=map(int,input().split())
if A+B<=P:
    print("Yes")
elif max(A,B)<=P and (A<=b or B<=a):
    print("Yes")
else:
    print("No")