h1,h2=map(int,input().split())
s1,s2=map(int,input().split())
v1,v2=map(int,input().split())
r,g,b=map(int,input().split())

V=max([r,g,b])
m=min([r,g,b])
S=255*(V-m)/V
if V==r:
    H=60*(g-b)/(V-m)
elif V==g:
    H=120+60*(b-r)/(V-m)
else:
    H=240+60*(r-g)/(V-m)

if H<0: H+=360

if h1<=H<=h2 and s1<=S<=s2 and v1<=V<=v2:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")