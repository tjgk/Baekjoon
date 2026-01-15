m,d=map(int,input().split())
print(max(d//m if d%m==0 else d//m+1,1))