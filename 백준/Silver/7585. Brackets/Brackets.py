while 1:
    a=input()
    tf=1
    if a=="#":
        break
    stack=[]
    for i in a:
        if i=="(" or i=="[" or i=="{":
            stack.append(i)
        elif i==")" or i=="]" or i=="}":
            if len(stack)==0:
                tf=0
                break
            elif i==")":
                b=stack.pop()
                if b!="(":
                    tf=0
                    break
            elif i=="]":
                b=stack.pop()
                if b!="[":
                    tf=0
                    break
            elif i=="}":
                b=stack.pop()
                if b!="{":
                    tf=0
                    break
    if len(stack)!=0:
        tf=0
    print("Legal" if tf==1 else "Illegal")