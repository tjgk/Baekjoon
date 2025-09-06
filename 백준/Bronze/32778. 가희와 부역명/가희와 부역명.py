a=input()
if "(" in a:
    a,b=a.split("(")
    print(a[:-1])
    print(b[:-1])
else:
    print(a)
    print("-")