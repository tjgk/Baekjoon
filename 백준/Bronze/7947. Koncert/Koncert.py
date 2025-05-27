from decimal import Decimal,ROUND_HALF_UP

for j in range(int(input())):
    r,g,b=0,0,0
    for i in range(10):
        x,y,z=map(int,input().split())
        r+=x
        g+=y
        b+=z
    R=Decimal(r/10).quantize(Decimal('1'),rounding=ROUND_HALF_UP)
    G=Decimal(g/10).quantize(Decimal('1'),rounding=ROUND_HALF_UP)
    B=Decimal(b/10).quantize(Decimal('1'),rounding=ROUND_HALF_UP)
    print(R,G,B)