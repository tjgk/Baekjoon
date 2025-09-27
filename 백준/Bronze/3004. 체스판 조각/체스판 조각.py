p=1
t=1
for i in range(int(input())):
    p+=t
    if i%2==0:
        t+=1
print(p)