a=[]
for i in range(int(input())):
    h,w=map(int,input().split())
    a.append(h*w)
print(max(a))