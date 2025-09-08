s=input()
r,c=1,len(s)
for i in range(2,len(s)//2+1):
    if len(s)%i==0 and i<=len(s)//i:
        r,c=i,len(s)//i
for i in range(r):
    for j in range(c):
        print(s[i+r*j],end="")