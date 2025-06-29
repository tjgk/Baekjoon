a=[]
for i in range(int(input())*2):
    a.append(input())
for i in range(len(a)//2):
    print(f"Case {i+1}: {a[2*i+1]}, {a[2*i]}")