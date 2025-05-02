s=int(input())
def f(x):
    a=[1]
    for i in range(2,x//2+2):
        if x%i==0:
            a.append(i)
    return sum(a)
while 1:
    if s==f(f(s)):
        if s!=f(s):
            r=[s,f(s)]
            break
    s+=1
print(r[0],r[1])