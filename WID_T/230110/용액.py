# 산성용액 = 1부터 1억
# 알칼리성용액 = -1부터 -1억
#  용액을 혼합한 용액의 특성값 0에 가까운 혼합 특성값 만들기

# 용액을 받을 때는 정렬된 순서로 받아온다.

# 모든 인덱스를 돌아서는 시간 초과,

# 절대값으로 오차값이 적은 값의 인덱스를 가져와서 비교?

# 음수끼리 더해서 0에 가깝거나 양수끼리 더해서 0에 가까울 수 있음,

# 값은 정렬되어있음 , 양 끝에서 포인터로 하나씩 줄어듦


n = int(input())

r = list(map(int, input().split()))


minimum = 1000000001

start, end = 0, n - 1  # 양쪽 포인트를 움직이는 기준점을 어디로 둬야할까? 적다면 계속 갱신
#
result = []
# 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재
i_sum = r[start] + r[end]
# 끝에서 끝 계산후에 어디 인덱스를 먼저 ?? 절대값이 큰 값 인덱스번호를 줄여준다,
while start != end:
    i_sum = r[start] + r[end]
    if minimum > abs(i_sum):
        minimum = abs(i_sum)
        result.append((abs(i_sum), start, end))
    if abs(r[start]) > abs(r[end]):
        start += 1
    else:
        end -= 1
result.sort()

start = result[0][1]
end = result[0][2]


print(r[start], r[end])
