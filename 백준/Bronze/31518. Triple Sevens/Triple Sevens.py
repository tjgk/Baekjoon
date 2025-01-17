n=int(input())
tf=1
for i in range(3):
    a=list(map(int,input().split()))
    if 7 not in a:
        tf=0
print(777 if tf==1 else 0)