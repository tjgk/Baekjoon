import sys
input=sys.stdin.readline
print=sys.stdout.write

def percolateUp(A,k):
    parent=(k-1)//2
    while k>0 and A[k]>A[parent]:
        A[k],A[parent]=A[parent],A[k]
        k=parent
        parent=(k-1)//2

def percolateDown(A,k):
    child=2*k+1
    right=2*k+2
    if child<=len(A)-1:
        if right<=len(A)-1 and A[child]<A[right]:
            child=right
        if A[k]<A[child]:
            A[k],A[child]=A[child],A[k]
            percolateDown(A,child)

n=int(input())
A=[]
for i in range(n):
    x=int(input())
    if x==0:
        if len(A)==0:
            print("0\n")
        else:
            print(str(A[0])+"\n")
            A[0]=A[-1]
            A.pop()
            percolateDown(A,0)
    else:
        A.append(x)
        percolateUp(A,len(A)-1)