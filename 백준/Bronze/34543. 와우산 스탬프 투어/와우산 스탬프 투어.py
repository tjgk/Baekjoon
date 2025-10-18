n=int(input())
w=int(input())
if n==5:
    print(10*n+70 if w<=1000 else 10*n+55)
elif n>=3:
    print(10*n+20 if w<=1000 else 10*n+5)
else:
    print(10*n if w<=1000 else max(10*n+-15,0))