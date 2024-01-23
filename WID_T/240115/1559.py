a = (
    "a",
    "b",
    "k",
    "d",
    "e",
    "g",
    "h",
    "i",
    "l",
    "m",
    "n",
    "ng",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "y",
)
arr = []
n = int(input())
for i in range(n):
    s = input()
    temp = []
    while len(s):
        if s[0:2] == "ng":
            temp.append(11)
            s = s[2:]
        else:
            temp.append(a.index(s[0]))
            s = s[1:]
    arr.append(temp)

arr.sort()
for i in arr:
    for j in i:
        print(a[j], end="")
    print()
