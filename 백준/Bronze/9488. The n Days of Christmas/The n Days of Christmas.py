import sys
input=sys.stdin.readline
print=sys.stdout.write
s=[0]
for i in range(1000000):
    s.append(s[-1]+i+1)
ss=[0,s[1]]
for i in range(1000000-1):
    ss.append(ss[-1]+s[i+2])
while 1:
    n=int(input())
    if n==0:
        break
    print(str(ss[n])+"\n")