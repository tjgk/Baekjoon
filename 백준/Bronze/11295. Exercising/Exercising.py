i=0
while 1:
    i+=1
    l=int(input())
    if l==0:break
    print("User",i)
    for j in range(int(input())):
        print(f"{int(input())*l/100000:.5f}")