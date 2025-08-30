import sys
input=sys.stdin.readline
print=sys.stdout.write

def naming(array):
    suits=["Clubs", "Diamonds", "Hearts", "Spades"]
    for i in array:
        if i%13==0:
            print(f"Ace of {suits[i//13-1]}\n")
        elif i%13==10:
            print((f"Jack of {suits[i//13]}\n"))
        elif i%13==11:
            print((f"Queen of {suits[i//13]}\n"))
        elif i%13==12:
            print((f"King of {suits[i//13]}\n"))
        else:
            print(f"{i%13+1} of {suits[i//13]}\n")
shuffles=[]
n=int(input())
shuffles.append(list(map(int,input().split())))

while len(shuffles)!=n or len(shuffles[-1])!=52:
    if len(shuffles[-1])!=52:
        shuffles[-1]+=list(map(int,input().split()))
    else:
        shuffles.append(list(map(int,input().split())))
beforeDeck=[i+1 for i in range(52)]
afterDeck=beforeDeck[:]
while 1:
    try:
        no=int(input())-1
        for i in range(52):
            afterDeck[i]=beforeDeck[shuffles[no][i]-1]
        beforeDeck=afterDeck[:]
        naming(afterDeck)
        print("\n")
    except:
        break
