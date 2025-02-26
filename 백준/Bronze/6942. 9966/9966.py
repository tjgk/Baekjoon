def r(x):
    x=str(x)
    y=""
    for i in "".join(reversed(x)):
        if i=="6":
            y+="9"
        elif i=="9":
            y+="6"
        elif i in ["0","1","8"]:
            y+=i
    if x==y:
        return 1
    else:
        return 0
s=0
for i in range(int(input()),int(input())+1):
    s+=r(i)
print(s)