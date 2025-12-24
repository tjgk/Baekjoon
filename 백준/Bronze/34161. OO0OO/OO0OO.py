import sys
print=sys.stdout.write

for i in range(3):
    x=input()
for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            for d in range(1,11):
                r=a*1000+b-d*1000
                if r>0:
                    print(str(r)+"\n")
                else:
                    print(str(-1)+"\n")
