r=input()
t=0
for i in range(int(input())):
    t+=1 if r[:5]==input()[:5] else 0
print(t)