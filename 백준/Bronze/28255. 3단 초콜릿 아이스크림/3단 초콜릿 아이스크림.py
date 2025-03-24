for i in range(int(input())):
    s=input()
    if len(s)%3==0:
        h=s[:len(s)//3]
    else:
        h=s[:len(s)//3+1]
    if s==h+"".join(reversed(h))+h:
        print(1)
    elif s==h+"".join(reversed(h))[1:]+h:
        print(1)
    elif s==h+"".join(reversed(h))+h[1:]:
        print(1)
    elif s==h+"".join(reversed(h))[1:]+h[1:]:
        print(1)
    else:
        print(0)