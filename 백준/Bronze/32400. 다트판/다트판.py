s=list(map(int,input().split()))
if s.index(20)==19:
    a=(20+s[-2]+s[0])/3
else:
    a=(20+s[s.index(20)-1]+s[s.index(20)+1])/3
b=sum(s)/20
if a>b:
    print("Alice")
elif a<b:
    print("Bob")
else:
    print("Tie")