import sys


input = sys.stdin.readline

words = input()
addChar = []
result = []
flag = 0
while words:
    char = words.pop()
    if char == ">":
        flag = 1
        addChar.append(char)
    elif char == "<":
        flag = 0
        addChar.append(char)
        result.append(addChar[::-1])
        addChar = []
