l,w=map(int,input().split())
if l>w or l*26<w:
    print("impossible")
else:
    for i in range(l-1):
        a=w//(l-i)
        print(chr(a+96),end="")
        w-=a
    print(chr(w+96))