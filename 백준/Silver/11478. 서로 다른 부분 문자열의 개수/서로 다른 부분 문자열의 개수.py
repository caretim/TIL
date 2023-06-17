import sys

s = list(map(str, sys.stdin.readline().rstrip("\n")))

temp = set() # set 자료 구조를 통해 중복을 제거

# 반복문을 통해 부분 문자열을 찾는다.
for i in range(len(s)):
    for j in range(len(s) + 1):
        # 부분 문자열이 있으면 temp에 저장
        if s[i:j]:
            temp.add("".join(s[i:j]))

print(len(temp))