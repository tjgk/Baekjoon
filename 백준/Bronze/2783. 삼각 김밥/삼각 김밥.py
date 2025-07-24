x,y=map(int,input().split())
for i in range(int(input())):
    a,b=map(int,input().split())
    if x/y>a/b:
        x,y=a,b
print(f"{1000*x/y}")