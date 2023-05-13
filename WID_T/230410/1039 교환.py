# from collections import deque

# n, k = map(int, input().split())

# sn = list(str(n))
# sn = list(map(int, sn))
# if len(sn) == 1:
#     print(-1)
#     exit()
# if len(sn) == 2 and "0" in sn:
#     print(-1)
#     exit()

# # 앞의 인덱스부터 뒤에 있는 인덱스중에 가장 큰값이랑 교환,
# # 만일 최대값이 이미 만들어졌을때, 맨 뒤의 자리수를 교체
# # except 0으로 시작 할 수 없음 0이 맨 앞으로 온다면, 실패
# # 한자리수도 실패 ,


# def bfs(sn, k):
#     idx = 0
#     n_length = len(sn)
#     while k:
#         change_num = -1
#         change_idx = -1
#         same = []
#         for i in range(n_length - 1, idx, -1):
#             if sn[idx] < sn[i]:  # 현재 인덱스뒤의 값중에 제일 큰값 갱신, 동일한 값있다면 기록,
#                 if change_num < sn[i]:
#                     change_num = sn[i]
#                     change_idx = i
#                     same = [i]
#                 elif change_num == sn[i]:
#                     same.append(i)
#         if change_num != -1:  # 최대값 찾았을 때. 현재인덱스와 찾은 값 바꿔주기 , 동일한 값이 존재할때,
#             if len(same) > 1:  # 같은 값이 여러개이며 뒤의 수 보다 크다면?  k횟수도 고려해야함,
#                 after_idx = idx + len(same) - 1
#                 if len(same) > k:  # 만약 동일한 값이 k번 이하라면,
#                     after_idx = idx + k
#                 check_idx = sn[idx : after_idx + 1]  # 동일한 값의 갯수만큼 숫자를 비교,
#                 check_idx.sort()  # 정렬해서 same과 순서 맞춰주기 ,
#                 for i in range(
#                     len(check_idx)
#                 ):  # 포문으로 꺼내면서 동일값 나오면 변경, 같은값이 여러개라도 순서는 상관없음, 순차적으로 들어오기떄문,
#                     if check_idx[i] == sn[idx]:
#                         change_idx = same[i]
#                         break
#             sn[change_idx] = sn[idx]
#             sn[idx] = change_num
#             # 본인의 수가 최대수이라면,
#             k -= 1
#             idx += 1

#         else:  # 지금 인덱스에서 뒤에서 더 큰수를 찾지 못하는 경우 k
#             find = 0
#             for i in range(len(sn) - 1):
#                 if sn[i] < sn[i + 1]:  # 최대값이 맞는지 확인, 각 인덱스가 내림차순으로 정렬되어있는지 확인,
#                     idx += 1
#                     check_idx = 0
#                     find = 1
#                     print("컨틴뉴반복")
#                     continue
#             if find == 0:
#                 for i in sn:  # 정렬된 수에서 동일한 값이 존재하는 경우,
#                     if sn.count(i) > 1:
#                         return sn
#                 noting1, noting2 = (
#                     sn[n_length - 1],
#                     sn[n_length - 2],
#                 )  # 최대값이고 정렬된 수에서 동일한 값이 없는 경우,
#                 # 동일 인덱스끼리 교환
#                 # 맨 뒤의 인덱스끼리 교환
#                 sn[n_length - 1] = noting2
#                 sn[n_length - 2] = noting1
#                 k -= 1
#                 idx += 1
#         return sn


# print(*bfs(sn, k), sep="")


from collections import deque

n, k = map(int, input().split())
len_n = len(str(n))


def bfs(n, k):
    q = deque()
    q.append((n, 0))
    visit = set()  # 방문리스트 생성 셋으로 중복방지,
    visit.add((n, 0))
    result = 0
    while q:
        new_n, count = q.popleft()
        str_n = list(str(new_n))
        if count == k:
            result = max(result, new_n)
            continue
        for i in range(len_n - 1):
            for j in range(i + 1, len_n):
                if i == 0 and int(str_n[j]) == 0:
                    continue
                str_n[i], str_n[j] = str_n[j], str_n[i]  # 현재 for문에서 나온 인덱스끼리 변환
                nn = int("".join(str_n))
                if (nn, count + 1) not in visit:
                    q.append((nn, count + 1))
                    visit.add((nn, count + 1))
                str_n[i], str_n[j] = str_n[j], str_n[i]  # 바꿨던 수 다시 원상복구
    return result if result else -1


print(bfs(n, k))
