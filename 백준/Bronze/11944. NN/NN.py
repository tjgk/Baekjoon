n,m=input().split()
m=int(m)
print((n*int(n))[:m] if len(n)*int(n)>m else n*int(n))