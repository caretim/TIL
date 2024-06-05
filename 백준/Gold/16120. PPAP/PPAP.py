
words = input()
words = list(words)
result = []

for i in words:
    result.append(i)
    if result[-4:] == ["P", "P", "A", "P"]:
        for __ in range(3):
            result.pop()


k = "".join(result)
if "PPAP" == k or "P" == k:
    print("PPAP")
else:
    print("NP")