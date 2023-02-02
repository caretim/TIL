n = "WrongAnswer"

for i in range(len(n)):
    if ord(n[i]) > 96:
        print(n[i].upper(), end="")
    else:
        print(n[i].lower(), end="")
