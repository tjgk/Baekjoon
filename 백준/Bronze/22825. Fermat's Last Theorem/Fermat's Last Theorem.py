import sys
input=sys.stdin.readline
print=sys.stdout.write

while 1:
    z=int(input())
    z3=z*z*z
    M=0
    if z==0:
        break
    for x in range(1,z):
        for y in range(x,z):
            xy=x*x*x+y*y*y
            if xy<=z3:
                if xy>M:
                    M=xy
            else:
                break
    print(str(z3-M)+"\n")