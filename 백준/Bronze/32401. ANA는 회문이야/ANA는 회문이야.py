n=int(input())
s=input()
cnt=0
a=''

for i in s:
    if i=="A" or i=="N":
        a+=i

for i in range(len(a)-2):
    if a[i:i+3]=="ANA":
        cnt+=1

print(cnt)