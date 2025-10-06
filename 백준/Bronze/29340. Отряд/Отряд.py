a=input()
b=input()
for i,j in zip(a,b):
    print(i if int(i)>int(j) else j,end="")