n,m,s=map(int,input().split())
print(s*(m) if s*(m)<s*(m+1)*(100-n)//100 else s*(m+1)*(100-n)//100)