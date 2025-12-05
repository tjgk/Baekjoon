s=int(input())
ma,f,mb=map(int,input().split())
if s<=ma+f+mb or s<=240:
    print("high speed rail")
else:
    print("flight")