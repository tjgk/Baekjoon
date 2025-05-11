s=input()
s=''.join(reversed(s))
i=0
c=0
while 1:
    if i>len(s)-1:
        break
    if s[i]=='=':
        if s[i+1]=="z":
            try:
                if s[i+2]=='d':
                    i+=3
                    c+=1
                else:
                    i+=2
                    c+=1
            except:
                i+=2
                c+=1
        else:
            i+=2
            c+=1
    elif s[i]=="-":
        i+=2
        c+=1
    elif s[i]=='j':
        try:
            if s[i+1]=="l" or s[i+1]=="n":
                i+=2
                c+=1
            else:
                i+=1
                c+=1
        except:
            i+=1
            c+=1
    else:
        i+=1
        c+=1
print(c)