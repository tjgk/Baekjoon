s=input()
t=[0,0]
for i in s:
    if i in ["a","e","i","o","u"]:
        t[0]+=1
        t[1]+=1
    elif i=="y":
        t[1]+=1
print(t[0],t[1])