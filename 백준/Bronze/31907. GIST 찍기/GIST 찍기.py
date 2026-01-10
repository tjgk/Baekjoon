k=int(input())
a=["G",".",".","."]
b=[".","I",".","T"]
c=[".",".","S","."]
for i in range(k):
    for j in a:
        print(j*k,end="")
    print()
for i in range(k):
    for j in b:
        print(j*k,end="")
    print()
for i in range(k):
    for j in c:
        print(j*k,end="")
    print()