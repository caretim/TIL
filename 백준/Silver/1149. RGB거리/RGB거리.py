n = int(input())


# cost_list=[0]*3

# 각 색별로 시작 진행한 값중 최소값으로 만들 수 있는 범위로 사용해야함,


house = [list(map(int, input().split())) for __ in range(n)]
# cost_list=[house[0]],[house[1]],[house[2]]

for i in range(1, n):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[n - 1]))
