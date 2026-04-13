i=0
while 1:
    i+=1
    n=int(input())
    if n==0: break
    n=round((n/2)*1.5)
    print(f"File #{i}")
    print(f"John needs {n//1860000 if n%1860000==0 else n//1860000+1} floppies.")
    print()