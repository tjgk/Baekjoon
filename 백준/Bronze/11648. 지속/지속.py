def f(x):
    r=1
    for i in x:
        r*=int(i)
    return str(r)
n=input()
c=0
while len(n)>1:
    c+=1
    n=f(n)
print(c)