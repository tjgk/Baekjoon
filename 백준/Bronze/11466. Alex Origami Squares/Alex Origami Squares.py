h,w=map(int,input().split())
a=[]
if w>=h:
    a.append(min(w/3,h))
else:
    a.append(min(w,h/3))
a.append(min(w/2,h/2))
print(max(a))