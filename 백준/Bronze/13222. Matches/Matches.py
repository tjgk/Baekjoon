n,w,h=map(int,input().split())
for i in range(n):
    l=int(input())
    print("YES" if (w**2+h**2)**0.5>=l else "NO")