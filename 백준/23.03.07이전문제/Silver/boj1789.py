# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	32306	13108	11190	42.349%
# 문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.


number= int(input())



num_cnt= 0

reselt= 0
for num in range(1,number+1):
    num_cnt+= num
    if num_cnt >number:
        break
    elif num_cnt == number:
        reselt=num
    reselt=num



print(reselt)


