n, check = map(int, input().split())

score = [[] for __ in range(n)]

# 앞등수중 같은 점수가 나올때, 또는 내가 앞나라와 점수가 같아서 동일 순위 일 때.

# 금메달 수가 더 많은 나라
# 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

for i in range(n):
    na, g, s, b = map(int, input().split())
    score[i] = [g * 10000 + s * 100 + b, na]

score.sort(key=lambda x: -x[0])

score[0].append(1)

count = 2
tie = (
    0  # 4개의 국가가 있고 1번국가 2번국가 3번이 금메달 2개 이고 4번 혼자  은메달 1개일때 1,2,3번국가는 공동 1등 4번국가는 4등이 됨
)
result = score[0][2]

for k in range(1, n):
    if score[k][0] == score[k - 1][0]:
        score[k].append(count - 1)
        tie += 1

    else:
        count = count + tie
        score[k].append(count)
        tie = 0
        count += 1

    if score[k][1] == check:
        result = score[k][2]


print(result)
