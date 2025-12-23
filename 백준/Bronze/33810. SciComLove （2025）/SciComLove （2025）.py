s=input()
t=0
for i,j in zip(s,"SciComLove"):
    if i!=j:
        t+=1
print(t)