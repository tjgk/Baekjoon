a=[]
while 1:
    t=float(input())
    if t==999:
        break
    a.append(t)
for i in range(len(a)-1):
    print(f"{a[i+1]-a[i]:.2f}")