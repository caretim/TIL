n = int(input())


s = list(map(int, input().split()))

# 처음부터 0으로 시작하는경우

# 연속한 돌상 구간의 점수를 구해야한다,

# 각 번호가 더해졌을때 시작점이 플러스일경우
# 시작점이 마이너스 일경우 카운트가 0으로 떨어지면 0으로 초기화
count1 = 0
count2= 0

dp =[]
for i in range(len(s)):
    if s[i] == 1:
        count1 += 1
        count2 -= 1
    elif s[i] == 2:
        count1 -= 1
        count2 += 1
    if count1 < 0:  # 음수로 숫자가 떨어질때 카운트 초기화 앞에구간을 버림
        count1 = 0
    if count2 < 0:  # 음수로 숫자가 떨어질때 카운트 초기화 앞에구간을 버림
        count2 = 0
    dp.append(count2)
    dp.append(count1)

print(max(dp))