import sys
input=sys.stdin.readline

w=int(input())
a=0
for i in range(int(input())):
    x,y=map(int,input().split())
    a+=x*y
print(a//w)