for i in range(int(input())):
    a=list(map(int,input().split()))
    a=list(filter(lambda x:x%2==0,a))
    a.sort()
    print(sum(a),a[0])