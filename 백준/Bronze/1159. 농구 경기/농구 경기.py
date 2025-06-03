d={chr(i+97):0 for i in range(26)}
for i in range(int(input())):
    a=input()
    d[a[0]]+=1

tf=0
for i in d.items():
    if i[1]>=5:
        print(i[0],end="")
        tf=1
if tf==0:
    print("PREDAJA")