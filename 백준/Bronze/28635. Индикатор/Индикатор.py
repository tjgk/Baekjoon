m=int(input())
a=int(input())
b=int(input())
if b-a<=m-a+b and b-a>=0:
    print(b-a)
else:
    print(m-a+b)