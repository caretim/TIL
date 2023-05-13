import heapq

import sys

input = sys.stdin.readline

# 딕셔너리로 최소힙 사용시 -1 최대힙 +1 마지막에 두리스트 set (최대 최소값만 구하면 됨,)
# for문으로 숫자 꺼내며 딕셔너리 값이 0일때, 마지막 출력 리스트에 담고 최대값,최소값꺼내기

for tc in range(int(input())):
    n = int(input().strip())

    min_list = []
    max_list = []
    num_dict = {}
    stop = 0
    for __ in range(n):
        c, num = input().split()
        num = int(num)
        if c == "I":
            heapq.heappush(min_list, num)
            heapq.heappush(max_list, -1 * num)
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        elif c == "D":
            if num == 1:
                try:
                    while True:
                        j = heapq.heappop(max_list) * -1
                        if num_dict[j] > 0:
                            num_dict[j] -= 1
                            break
                except:
                    pass
            elif num == -1:
                try:
                    while True:
                        j = heapq.heappop(min_list)
                        if num_dict[j] > 0:
                            num_dict[j] -= 1
                            break
                except:
                    pass

    result = []
    for k, v in num_dict.items():
        if v > 0:
            result.append(k)

    if len(result) == 0:
        print("EMPTY")
    else:
        print(max(result), min(result))