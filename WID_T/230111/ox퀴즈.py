quiz = ["3 - 4 = -3", "5 + 6 = 11"]
answer = []
for i in quiz:
    char = i.replace(" ", "")
    a, b = char.split("=")
    if eval(a) == int(b):
        answer.append("O")
    else:
        answer.append("X")
print(answer)
