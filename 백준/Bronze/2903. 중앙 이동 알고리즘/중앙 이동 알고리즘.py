n=int(input())
a=[2,3,5]
while len(a)!=16:
    a.append(a[-1]+a[-1]-1)
print(a[n]**2)