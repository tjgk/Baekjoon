a=[]
for i in range(3):
    a.append(int(input()))
tf=1
if a[0] not in [1,3]:
    tf=0
if a[1] not in [6,8]:
    tf=0
if a[2] not in [2,5]:
    tf=0
print("JAH" if tf==1 else "EI")