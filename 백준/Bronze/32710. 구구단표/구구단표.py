n=int(input())
a=[1]
for i in range(2,10):
    for j in range(1,10):
        a.append(i*j)
print(1 if n in a else 0)