T,S=[],[]
for i in range(4):
    T.append(list(map(int,input().split())))
for i in range(4):
    S.append(list(map(int,input().split())))
t,s=[],[]
for i in range(6):
    a,b="",""
    for j in range(4):
        a+=str(T[j][i])
        b+=str(S[j][i])
    t.append(a)
    s.append(b)
x=int(t[0],2)*10+int(t[1],2)+int(s[0],2)*10+int(s[1],2)
y=int(t[2],2)*10+int(t[3],2)+int(s[2],2)*10+int(s[3],2)
z=int(t[4],2)*10+int(t[5],2)+int(s[4],2)*10+int(s[5],2)
if z>=60:
    z-=60
    y+=1
if y>=60:
    y-=60
    x+=1
if x>=24:
    x-=24
r=""
for i in x,y,z:
    if len(str(i))==2:
        r+=str(i)
    else:
        r+="0"+str(i)
ans=[]
for i in r:
    k="0"*(4-len(bin(int(i))[2:]))+bin(int(i))[2:]
    ans.append(k)
for i in range(4):
    print(ans[0][i],ans[1][i],ans[2][i],ans[3][i],ans[4][i],ans[5][i])