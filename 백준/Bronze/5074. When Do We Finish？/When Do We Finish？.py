while 1:
    a,b=input().split()
    if a+b=="00:0000:00":
        break
    a=list(map(int,a.split(":")))
    b=list(map(int,b.split(":")))
    m=(a[1]+b[1])%60
    h=(a[0]+b[0]+(a[1]+b[1])//60)%24
    d=(a[0]+b[0]+(a[1]+b[1])//60)//24
    if d==0:
        print(f"{h:02}:{m:02}")
    else:
        print(f"{h:02}:{m:02} +{d}")