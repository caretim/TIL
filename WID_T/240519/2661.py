import sys

def check(s):
    for i in range(1, len(s), 2):
        for j in range(len(s)):
            if j + i < len(s):
                temp = s[j : j + i + 1]
                size = len(temp)
                left = temp[0: size // 2]
                right = temp[size // 2 : size + 1]
                if left == right:
                    return False
    return True

def Traking(depth, reuslt):
    if depth == n:
        print(reuslt)
        sys.exit(0)
    for i in range(1, 4):
        if check(reuslt + str(i)):
            Traking(depth + 1, reuslt + str(i))

n = int(sys.stdin.readline())
Traking(0, '')