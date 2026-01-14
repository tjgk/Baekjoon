a,b=map(int,input().split())
d=int(input())
print((a*b//12 if a*b%12==0 else a*b//12+1)*d)