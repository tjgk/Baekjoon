b=input()
M=[int(b),0]

for i in range(int(input())):
    d=input()
    c,e,f=0,0,0
    for i in range(4):
        c+=(int(b[i])-int(d[i]))**2
    for i in range(2):
        e+=(int(b[i+4])-int(d[i+4]))**2
    for i in range(2):
        f+=(int(b[i+6])-int(d[i+6]))**2
    if c*e*f>M[1]:
        M[1]=c*e*f
        M[0]=int(d)
    elif c*e*f==M[1]:
        if M[0]>int(d):
            M[0]=int(d)

print(M[0])