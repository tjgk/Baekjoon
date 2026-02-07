n,s=input().split()
for i in range(int(n)):
    if ord(s[i])+(2**i)%26<=90:
        print(chr(ord(s[i])+(2**i)%26),end="")
    else:
        print(chr(ord(s[i])+(2**i)%26-26),end="")