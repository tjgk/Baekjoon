n=int(input())
a=input()
r=a[-1]
for i in reversed(a[:-1]):
    if r=="A":
        if i=="A" or i=="C":
            r="A"
        elif i=="G":
            r="C"
        else:
            r="G"
    elif r=="G":
        if i=="A":
            r="C"
        elif i=="G":
            r="G"
        elif i=="C":
            r="T"
        else:
            r="A"
    elif r=="C":
        if i=="A":
            r="A"
        elif i=="G":
            r="T"
        elif i=="C":
            r="C"
        else:
            r="G"
    else:
        if i=="A" or i=="C":
            r="G"
        elif i=="G":
            r="A"
        else:
            r="T"
print(r)