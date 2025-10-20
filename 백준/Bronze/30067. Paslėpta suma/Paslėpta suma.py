a=[]
for i in range(10):
    a.append(int(input()))
for i in a:
    if sum(a)//2==i:
        print(i)
        break