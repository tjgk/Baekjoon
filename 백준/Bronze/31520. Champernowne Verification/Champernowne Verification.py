n=input()
t=-1
for i in range(len(n)):
    if str(i+1)!=n[i]:
        t=0
        break
print(-1 if t==0 else n[-1])