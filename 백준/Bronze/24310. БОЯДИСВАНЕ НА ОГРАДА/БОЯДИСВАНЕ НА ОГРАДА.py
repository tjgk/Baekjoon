a,b,c,d=map(int,input().split())
a,b=min(a,b),max(a,b)
c,d=min(c,d),max(c,d)
print(b-a+d-c+2-max(min(b,d)-max(a,c)+1,0))