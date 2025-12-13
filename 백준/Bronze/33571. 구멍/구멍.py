h=0
for i in input():
    if i=="B":
        h+=2
    elif i in ["A","a","b","D","d","e","g","O","o","P","p","Q","q","R","@"]:
        h+=1
print(h)