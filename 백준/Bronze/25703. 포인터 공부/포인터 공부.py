n=int(input())
print("int a;")
for i in range(n):
    if i==0:
        print("int *ptr = &a;")
    elif i==1:
        print("int **ptr2 = &ptr;")
    else:
        print(f"int {'*'*(i+1)}ptr{i+1} = &ptr{i};")