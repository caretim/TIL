# 완주하지 못한 선수


start = list(input().split())

end = list(input().split())

dict = {}


for name in start:
    dict[name] = dict.get(name, 0) + 1  # 딕셔너리에 출발한 사람들의 이름이 나올때마다 이름의 키에 값 +1


for name in end:
    dict[name] = dict.get(name, 0) - 1  # 딕셔너리에 도착한 사람들의 이름이 나올때마다 이름의 키에 값 -1


for runner in start:  #   출발해서 도착했다면 딕셔너리의 값은 0이여야함
    if dict[runner] >= 1:  #   도착하지 못했다면 딕셔너리의 값은 1 이상
        result = runner


print(result)


# if name not in end_dc:
#     end_dc[name] = 1
# else:
#     end_dc[name] += 1

# for runner in start:
#     if dict[runner] >= 1:
#         result = runner
#         # re.append(runner)
#     # elif dict[runner] > 1:
#     #     dict[runner] -= 1

# # for runner in start:
# #     if end_dc[runner] > 0:
# #         end_dc[runner] -= 1
# # result = set(re)
