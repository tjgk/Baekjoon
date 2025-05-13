w=int(input())
l=int(input())
h=int(input())
print('good' if min(w,l)>=2*h and min(w,l)*2>=max(w,l) else 'bad')