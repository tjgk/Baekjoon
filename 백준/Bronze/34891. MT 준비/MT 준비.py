n,m=map(int,input().split())
print(n//m if n%m==0 else n//m+1)