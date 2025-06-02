ans=[0 for i in range(26)]
for i in range(int(input())):
    a,b=input().split()
    d={chr(i+97) : 0 for i in range(26)}
    for j in range(26):
        if a.count(chr(j+97))>d[chr(j+97)]:
            d[chr(j+97)]+=a.count(chr(j+97))-d[chr(j+97)]
    for j in range(26):
        if b.count(chr(j+97))>d[chr(j+97)]:
            d[chr(j+97)]+=b.count(chr(j+97))-d[chr(j+97)]
    for j in range(26):
        ans[j]+=d[chr(j+97)]
for i in ans:
    print(i)