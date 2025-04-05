n=int(input())
c=0
for b in range(1,501):
    for a in range(b,501):
        if a**2==b**2+n:
            c+=1
print(c)