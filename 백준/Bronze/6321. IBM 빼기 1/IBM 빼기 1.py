n=int(input())
for i in range(n):
    s=input()
    print(f"String #{i+1}")
    for j in s:
        print(chr(ord(j)+1) if j!="Z" else "A",end="")
    if i+1==n:
        break
    print()
    print()