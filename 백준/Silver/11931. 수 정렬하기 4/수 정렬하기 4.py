import sys
input=sys.stdin.readline
print=sys.stdout.write
a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
a.sort()
for i in range(n):
    print(str(a[-1*(i+1)])+"\n")