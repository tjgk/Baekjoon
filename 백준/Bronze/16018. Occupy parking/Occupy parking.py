n=int(input())
a=input()
b=input()
cnt=0
for i in range(n):
    if a[i]=="C" and b[i]=="C":
        cnt+=1
print(cnt)