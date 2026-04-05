import math

def f(x,y):
    i=-1
    while x>y:
        i+=1
        y*=5
    return i

for i in range(int(input())):
    e,a=map(int,input().split())
    print(f"Data Set {i+1}:")
    if e<=a:
        print("no drought")
    else:
        print("mega "*f(e,a)+"drought")
    print()