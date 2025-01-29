a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)>sum(b):
    print("Algosia")
elif sum(a)<sum(b):
    print("Bajtek")
else:
    tf=0
    for i in range(10,0,-1):
        if a.count(i)>b.count(i):
            tf=1
            print("Algosia")
            break
        elif a.count(i)<b.count(i):
            tf=1
            print("Bajtek")
            break
    if tf==0:
        print("remis")