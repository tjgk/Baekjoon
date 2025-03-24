t=input()
k=ord(t[0])^ord("C")
for i in t:
    print(chr(ord(i)^k),end="")