for i in range(int(input())):
    c=0
    a=input()
    b=input()
    for i,j in zip(a,b):
        if i!=j: c+=1
    print(f"Hamming distance is {c}.")