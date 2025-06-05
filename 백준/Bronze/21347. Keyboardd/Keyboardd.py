s=input()
t=input()
S,T={},{}
r=[]
for i in s:
    if i not in S:
        S[i]=1
    else:
        S[i]+=1
for i in t:
    if i not in T:
        T[i]=1
    else:
        T[i]+=1
for i in S.keys():
    if S[i]!=T[i]:
        r.append(i)
print("".join(r))