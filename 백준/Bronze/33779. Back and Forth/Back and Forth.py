s=input()
p=0
for i in range(len(s)//2):
    if s[i]!=s[-1*(i+1)]:
        print("boop")
        p=1
        break
if p==0:
    print("beep")