for i in range(int(input())):
    p=0
    a=[0 for i in range(26)]
    for j in input():
        a[ord(j)-65]+=1
    for j in range(26):
        if a[j]==0:
            p+=j+65
    print(p)