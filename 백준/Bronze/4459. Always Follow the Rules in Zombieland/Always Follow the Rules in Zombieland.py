a=[]
for i in range(int(input())):
    a.append(input())
for i in range(int(input())):
    n=int(input())
    print(f"Rule {n}: {a[n-1]}" if 1<=n<=len(a) else f"Rule {n}: No such rule")