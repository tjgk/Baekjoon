x=input()
y=input()
a=[]
a.append(abs(ord(y[0])-ord(x[0])))
a.append(abs(int(y[1])-int(x[1])))
a.sort()
print(a[0],a[1])