c=0
for i in range(int(input())):
    c+=1 if input().count("CD")==0 else 0
print(c)