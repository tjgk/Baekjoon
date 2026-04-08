n,m,k=map(int,input().split())
print(n*(m//k+k-1) if m>=k else n*m)