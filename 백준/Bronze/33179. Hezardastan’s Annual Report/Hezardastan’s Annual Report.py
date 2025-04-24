n=int(input())
a=list(map(int,input().split()))
r=0
for i in a:
    r+=i if i%2==0 else i+1
print(r//2)