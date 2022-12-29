# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    num_range = len(phone_number)
    answer = []
    for j in range(num_range):
        if j < num_range - 4:
            answer.append("*")
        else:
            answer.append(phone_number[j])
    return "".join(answer)


phone_number = "01033334444"
print(solution(phone_number))
