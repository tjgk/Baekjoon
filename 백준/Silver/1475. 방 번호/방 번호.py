n=input()
a=[0 for i in range(10)]
for i in n:
    a[int(i)]+=1
a[6]+=a[9]
a.pop()
a[6]=a[6]//2 if a[6]/2==a[6]//2 else a[6]//2+1
print(max(a))