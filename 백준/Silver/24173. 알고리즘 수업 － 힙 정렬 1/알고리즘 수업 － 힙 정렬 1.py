def heap_sort(A):
    global cnt,a,b
    build_min_heap(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        cnt+=1
        if cnt==t:
            a,b=A[0],A[i]
        heapify(A,0,i)

def build_min_heap(A,n):
    for i in range((n-1)//2,-1,-1):
        heapify(A,i,n)

def heapify(A,k,n):
    global cnt,a,b
    left=2*k+1
    right=2*k+2
    if right<n:
        if A[left]<A[right]:
            smaller=left
        else:
            smaller=right
    elif left<n:
        smaller=left
    else:
        return
    if A[smaller]<A[k]:
        A[k],A[smaller]=A[smaller],A[k]
        cnt+=1
        if cnt==t:
            a,b=A[k],A[smaller]
        heapify(A,smaller,n)

n,t=map(int,input().split())
A=list(map(int,input().split()))
cnt=0

heap_sort(A)
print(-1) if cnt<t else print(min(a,b),max(a,b))