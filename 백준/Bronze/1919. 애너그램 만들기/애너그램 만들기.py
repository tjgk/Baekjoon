a=input()
b=input()
s=0
for i in range(26):
    s+=max(a.count(chr(97+i)),b.count(chr(97+i)))-min(a.count(chr(97+i)),b.count(chr(97+i)))
print(s)