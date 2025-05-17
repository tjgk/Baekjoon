import sys
input=sys.stdin.readline
print=sys.stdout.write

a,b=0,0
for i in range(int(input())):
    x,y=map(int,input().split())
    a+=x
    b+=y
    print(str(a-b)+"\n")