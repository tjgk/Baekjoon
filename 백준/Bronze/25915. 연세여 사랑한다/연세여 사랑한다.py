s=input()+"ILOVEYONSEI"
t=0
for i in range(len(s)-1):
    t+=abs(ord(s[i+1])-ord(s[i]))
print(t)