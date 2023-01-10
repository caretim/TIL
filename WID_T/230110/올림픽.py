n, check = map(int, input().split())

score = []

# 앞등수중 같은 점수가 나올때, 또는 내가 앞나라와 점수가 같아서 동일 순위 일 때.

for __ in range(n):
    na, g, s, b = map(int, input().split())
    score.append(((g * 3 + s * 2 + b), na))


score.sort()

score[0].append(1)
for k in range(n):
    score[k].append(count)
    if score[k]
        
