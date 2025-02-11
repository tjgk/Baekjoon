for i in range(int(input())):
    x,y=input().split()
    v=[y.count("B")*2,y.count("C"),y.count("M")*4,y.count("W")*3]
    if v.count(max(v))>=2:
        print(f"{x}: There is no dominant species")
    else:
        m=max(v)
        if m==v[0]:
            print(f"{x}: The Bobcat is the dominant species")
        elif m==v[1]:
            print(f"{x}: The Coyote is the dominant species")
        elif m==v[2]:
            print(f"{x}: The Mountain Lion is the dominant species")
        else:
            print(f"{x}: The Wolf is the dominant species")