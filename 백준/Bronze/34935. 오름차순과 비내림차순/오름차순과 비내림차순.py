n=int(input())
a=list(map(int,input().split()))
print(1 if a==sorted(a) and len(a)==len(set(a)) else 0)