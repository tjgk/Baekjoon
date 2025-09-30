a=list(map(int,input().split(":")))
b=list(map(int,input().split(":")))
x=a[0]*3600+a[1]*60+a[2]
y=b[0]*3600+b[1]*60+b[2]
if x>=y:
    y+=24*3600
t=y-x
print(f"{t//3600:02}:{(t%3600)//60:02}:{t%60:02}")