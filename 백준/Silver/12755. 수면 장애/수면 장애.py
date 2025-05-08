n=int(input())
a=0
for i in range(9):
    if n<=a:
        l=i
        break
    else:
        a+=(i+1)*9*10**i
c=a-l*9*10**(l-1)
i=10**(l-1)
while 1:
    if n<=c:
        print(str(i-1)[l-1-(c-n)])
        break
    else:
        c+=len(str(i))
        i+=1