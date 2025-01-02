n,c=map(int,input().split())
t=0
for i in range(n):
    m,s=map(int,input().split(":"))
    t+=m*60+s
t-=(n-1)*c

print(f"{t//3600:02}:{t%3600//60:02}:{t%60:02}")