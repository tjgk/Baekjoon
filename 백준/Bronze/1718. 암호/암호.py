a=input()
p=input()
for i in range(len(a)):
    if a[i]==" ":
        print(" ",end="")
    elif ord(a[i])>ord(p[i%len(p)]):
        print(chr(ord(a[i])-ord(p[i%len(p)])+96),end="")
    else:
        print(chr(ord(a[i])-ord(p[i%len(p)])+122),end="")