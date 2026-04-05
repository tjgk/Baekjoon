n=int(input())
s=0
while n!=1:
    if n%2==0:
        s+=1
        n//=2
    else:
        n=n*3+1
        s+=1
print(s)