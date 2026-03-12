a=[]
for i in range(6):
    a.append(input())
    if a[i][-1]==" ":
        a[i]=a[i][:-1]
print(f"Latitude {len(a[0])}:{len(a[1])}:{len(a[2])}")
print(f"Longitude {len(a[3])}:{len(a[4])}:{len(a[5])}")