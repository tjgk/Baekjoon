for i in range(int(input())):
    a=[0 for _ in range(26)]
    for j in input():
        a[ord(j)-97]+=1
    a.sort()
    if a[-3]==0:
        print(0)
    else:
        print(sum(a[:-2]))