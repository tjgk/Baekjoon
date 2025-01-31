a=input()
b=""
t=0
for i in a[::-1]:
    t+=1
    b+=i
    if t%3==0:
        b+=","
if b[-1]==",":
    b=b[:-1]
for i in b[::-1]:
    print(i,end="")