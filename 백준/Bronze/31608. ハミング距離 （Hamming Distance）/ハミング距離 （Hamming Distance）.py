n=int(input())
a=input()
b=input()
t=0
for i,j in zip(a,b):
    if i!=j:
        t+=1
print(t)