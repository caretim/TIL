
import sys

from itertools import combinations



n =int(input())
result = []
for i in range(1,11): # 각 숫자별로 조합리스트를 만든다,
    for com in combinations(range(0,10),i):
        # print(com)
        arr = list(com)
        arr.sort(reverse=True) # 각 숫자별 리스트들을 내림차순으로 모두 정렬 
        result.append(int("".join(map(str, arr)))) # 조합별로 나오는 수를 정답에 넣은 후 정렬 ,
result.sort()

if n >= len(result):
    print(-1)
else:
    print(result[n])

