def solution(x):
    answer = True
    str_x = str(x)
    count = 0
    for i in str_x:
        count += int(i)
    if x % count != 0:
        answer = False
    return answer
