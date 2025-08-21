n,m=map(int,input().split())
a=list(map(int,input().split()))
o=list(map(int,input().split()))
s=[0 for i in range(n)]
for i in range(m):
    s[o[i]-1]=a[o[i]-1]
for i in range(n):
    if n>=3:
        if s[i]==0:
            if i==0:
                s[i]=list({1,2,3}-{s[1]}-{a[i]})[0]
            elif i==n-1:
                s[i]=list({1,2,3}-{s[n-2]}-{a[i]})[0]
            else:
                s[i]=list({1,2,3,4}-{s[i-1]}-{s[i+1]}-{a[i]})[0]
    elif n==2:
        if s[i]==0:
            if i==0:
                s[i]=list({1,2,3}-{s[1]}-{a[i]})[0]
            else:
                s[i]=list({1,2,3}-{s[0]}-{a[i]})[0]
    elif n==1:
        if s[i]==0:
            s[i]={1,2}-{a[i]}
for i in s:
    print(i,end=" ")