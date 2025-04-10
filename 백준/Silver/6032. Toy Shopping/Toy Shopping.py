import sys
input=sys.stdin.readline

d=[]
for i in range(int(input())):
    j,p=map(int,input().split())
    d.append([i+1,j,p,j/p])
d=sorted(d,key=lambda x:x[3],reverse=1)
print(d[0][2]+d[1][2]+d[2][2])
for i in range(3):
    print(d[i][0])