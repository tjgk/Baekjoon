n=int(input())
s=input()
c=0
for i in s:
    c+=2 if i in ["j","i"] else 1
print(c)