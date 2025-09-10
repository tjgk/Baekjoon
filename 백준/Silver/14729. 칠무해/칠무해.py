import sys
input=sys.stdin.readline
a=[]
for i in range(int(input())):
    a.append(float(input()))
a.sort()
for i in range(7):
    print(f"{a[i]:.3f}")