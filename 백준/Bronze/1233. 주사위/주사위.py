s=[]
a,b,c=map(int,input().split())
for i in range(a):
    for j in range(b):
        for k in range(c):
            s.append(i+j+k+3)
S=[0 for i in range(max(s)+1)]
for i in s:
    S[i]+=1
print(S.index(max(S)))