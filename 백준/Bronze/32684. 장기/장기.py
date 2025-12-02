a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=a[0]*13+a[1]*7+a[2]*5+a[3]*3+a[4]*3+a[5]*2
B=b[0]*13+b[1]*7+b[2]*5+b[3]*3+b[4]*3+b[5]*2+1.5
print("cocjr0208" if A>B else "ekwoo")