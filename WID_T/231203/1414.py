dict = {
    "a": "a",
    "b": "b",
    "k": "c",
    "d": "d",
    "e": "e",
    "g": "f",
    "h": "g",
    "i": "h",
    "l": "i",
    "m": "j",
    "n": "k",
    "x": "l",
    "o": "m",
    "p": "n",
    "r": "o",
    "s": "p",
    "t": "q",
    "u": "r",
    "w": "s",
    "y": "t",
}


def s_change(alp):
    return dict[alp]


n = int(input())

word_list = []

result = []
for __ in range(n):
    w = input().rstrip()
    word = w.replace("ng", "x")
    word_list.append(word)

result = sorted(word_list, key=lambda x: x)

for word in result:
    print(word.replace("x", "ng"))
