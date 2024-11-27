import sys
input=sys.stdin.readline
stack=[]
for i in range(int(input())):
    t=int(input())
    if t!=0:
        stack.append(t)
    else:
        del stack[-1]
print(sum(stack))