# 백만까지 채 만들기 소수체에 거를때   -> 진수3~10 변경 ->
# 변경한값을 문자열 인덱스로 조작해서 체에 있는지 조사하기 or 소수인덱스로만들자
# 숫자에 0이 있다면 제외시켜주기 인덱스에서 조작

# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.

# 0이 들어가지않는 인덱스 , 201202013,체에 있는 값을 찾기

# 소수양쪽 0


from collections import deque

max_num = 1000001

check_num = [0] * 1000001
count = 0

r = int(max_num**0.5)

for i in range(2, r):
    if check_num[i] == 0:
        for j in range(i + i, len(check_num), i):
            check_num[j] = 1
            count += 1

print(count)

# 진수 변경
# 뒷자리부터 3으로? 나누기?가 아니고 3으로 나눈 몫을 계속 나눠가며 나머지를 넣어주기

# for문으로 리스트를 돌면서? 간다? 아니면
# def solution(n, k):
#     num = deque(list)
#     while n==0:
#         n= n//k
#         y= n%k
#         num.appendleft(y)


#     return answer
