n=int(input())
s=input()
t=input()
x,y=0,0
for i,j in zip(s,t):
    if i==j:
        continue
    elif [i,j]==["R","S"] or [i,j]==["S","P"] or [i,j]==["P","R"]:
        x+=1
    else:
        y+=1
print(x,y)