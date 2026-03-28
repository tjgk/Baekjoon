n=[0]
for i in range(1,101):
    n.append(n[-1]+i*i)
while 1:
    a=int(input())
    if a==0:
        break
    print(n[a])