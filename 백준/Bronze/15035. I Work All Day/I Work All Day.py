n=int(input())
a=list(map(int,input().split()))
t=int(input())
b=[]
for i in a:
    b.append(t%i)
print(a[b.index(min(b))])