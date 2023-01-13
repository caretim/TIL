# 한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.

# 9 3 1
# 최대힙으로 가장 큰 수 중간수 계속 정렬시키면서 값 빼주기?

# 최대힙 또는 람다함수로 값 계속 정렬시켜주며 9,3,1씩 뺴주기,

import heapq

n = int(input())

scv = list(map(int, input().split()))

count = 0
damage = [9, 3, 1]

# scv가 3마리가 아니라면 ? 순서에따라 카운트 돌아가면서
while True:
    scv.sort(reverse=True)
    print(scv)
    if scv[0] <= 0:
        break
    for i in range(n):
        scv[i] -= damage[i]
    count += 1
print(count)
