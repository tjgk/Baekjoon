import sys
input=sys.stdin.readline
print=sys.stdout.write

for i in range(int(input())):
    a,b,c=map(int,input().split())
    if c%2==0:
        if 2*b+a>=c:
            print("YES\n")
        else:
            print("NO\n")
    else:
        if a==0:
            print("NO\n")
        elif 2*b+a>=c:
            print("YES\n")
        else:
            print("NO\n")