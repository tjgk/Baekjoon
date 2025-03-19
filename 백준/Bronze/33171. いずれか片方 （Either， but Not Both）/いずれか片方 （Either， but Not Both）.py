n=int(input())
a=int(input())
b=int(input())
c=0
for i in range(1,n+1):
    if int(i%a==0)+int(i%b==0)==1:
        c+=1
print(c)