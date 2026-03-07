pi=3.141592653589793

for i in range(int(input())):
    b,w=input().split()
    b=int(b)
    w=float(w)
    s=0
    for j in range(b):
        s+=(float(input()))**3*(4/3)*pi
    print(f"Data Set {i+1}:")
    print(f"Yes" if s/1000>w else "No")
    print()