n=int(input())
l=[]
for i in range(n):
    l.append(input())
for i in range(int(input())):
    s,e=map(int,input().split())
    for j in range(s,e+1):
        print(l[j-1])