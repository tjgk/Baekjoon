n=int(input())
l=[n]
i=0
while 1:
    i+=1
    n=(((n%1000)//100)*10+((n%100)//10))**2
    if n in l:
        print(i)
        break
    else:
        l.append(n)