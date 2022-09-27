n, m = map(int, input().split())


nlist = list(map(int, input().split()))


insnum = 0  # # 값비교를 위한 index[0...m-1]의 합
for k in range(m):  # 범위의 합 구하기 위한 for문
    insnum += nlist[k]

maxn = insnum  # 최댓값

ic = 0  # 먼저 들어온 값을 빼주기 위한 변수
for j in range(m, n):
    nsum = insnum - nlist[ic] + nlist[j]  # 처음 들어온 인덱스 값을 빼준 후  뒤에 들어올 값 nlist[j]를 더해준다
    insnum = nsum  # 계산 된 값을 insnum 변수에 갱신
    if nsum > maxn:  # 계산 된 값이 maxn(최댓값)보다 크다면 최댓값 갱신
        maxn = nsum
    ic += 1  # 먼저 들어온 값의 인덱스를 증가시키기 위해 ic를 1씩 증가시켜준다.
print(maxn)


# moneys = 0

# # for k in range(n - 1, m - 1, -1):
# #     daily = 0
# #     for i in range(m):
# #         daily += nlist[k - i]
# #     if moneys < daily:
# #         moneys = daily

# # print(moneys)
# print(moneys)
