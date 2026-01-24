n=int(input())
m=[10,10]
for i in range(1,11):
    for j in range(1,11):
        if i+j<sum(m) and i*j>=n:
            m[0]=i
            m[1]=j
print(m[0],m[1])