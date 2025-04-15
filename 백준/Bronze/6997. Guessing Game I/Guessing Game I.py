for i in range(int(input())):
    s,g=input().split()
    c,S,G=0,{},{}
    for j in range(4):
        if s[j]==g[j]:
            c+=1
        else:
            if s[j] in S:
                S[s[j]]+=1
            else:
                S[s[j]]=1
            if g[j] in G:
                G[g[j]]+=1
            else:
                G[g[j]]=1
    sq=0
    for i in S.keys():
        if i in G:
            sq+=min(S[i],G[i])
    print(f"For secret = {s} and guess = {g}, {c} circles and {sq} squares will light up.")