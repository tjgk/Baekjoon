s=""
while 1:
    try:
        s+=input()
    except:
        s=s.split(",")
        print(sum(list(map(lambda x:int(x),s))))
        break