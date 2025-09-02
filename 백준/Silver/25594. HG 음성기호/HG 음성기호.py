import sys

d = {
"a": "aespa",
"b": "baekjoon",
"c": "cau",
"d": "debug",
"e": "edge",
"f": "firefox",
"g": "golang",
"h": "haegang",
"i": "iu",
"j": "java",
"k": "kotlin",
"l": "lol",
"m": "mips",
"n": "null",
"o": "os",
"p": "python",
"q": "query",
"r": "roka",
"s": "solvedac",
"t": "tod",
"u": "unix",
"v": "virus",
"w": "whale",
"x": "xcode",
"y": "yahoo",
"z": "zebra"
}

s=sys.stdin.readline().rstrip("\n")
i,p=0,0
r=[]

while i<len(s):
    if d[s[i]]==s[i:i+len(d[s[i]])]:
        r.append(s[i])
        i+=len(d[s[i]])
    else:
        print("ERROR!")
        p=1
        break

if p==0:
    print("It's HG!")
    print("".join(r))