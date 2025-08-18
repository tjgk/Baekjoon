n,k=map(int,input().split())
g=list(map(int,input().split()))
for i in g:
    if i/n<0.05:
        print(1,end=" ")
    elif i/n<0.12:
        print(2,end=" ")
    elif i/n<0.24:
        print(3,end=" ")
    elif i/n<0.41:
        print(4,end=" ")
    elif i/n<0.61:
        print(5,end=" ")
    elif i/n<0.78:
        print(6,end=" ")
    elif i/n<0.9:
        print(7,end=" ")
    elif i/n<0.97:
        print(8,end=" ")
    else:
        print(9,end=" ")