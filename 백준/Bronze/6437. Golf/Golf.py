i=0
while 1:
    i+=1
    p,s=map(int,input().split())
    if p==s==0:break
    print(f"Hole #{i}")
    if s==1:
        print("Hole-in-one.")
    elif p-s==3:
        print("Double eagle.")
    elif p-s==2:
        print("Eagle.")
    elif p-s==1:
        print('Birdie.')
    elif p==s:
        print('Par.')
    elif p-s==-1:
        print('Bogey.')
    else:
        print('Double Bogey.')
    print()