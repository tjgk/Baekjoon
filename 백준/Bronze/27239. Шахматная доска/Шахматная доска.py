a=[]
for i in range(1,9):
    for j in ["a","b","c","d","e","f","g","h"]:
        a.append(j+str(i))
print(a[int(input())-1])