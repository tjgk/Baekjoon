import sys
input=sys.stdin.readline
print=sys.stdout.write

for i in range(int(input())):
    a,b=map(int,input().split())
    if a+b==0:
        print(str(0)+"\n")
    else:
        r=0
        while 1:
            if a*4<b:
                a+=1
                r+=1
            elif a*3>b:
                b+=1
                r+=1
            else:
                print(str(r)+"\n")
                break