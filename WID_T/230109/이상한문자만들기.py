s = " t r y he llo WORld "


def solution(s):
    count = 0
    answer = ""
    for i in s:
        if i == " ":
            count = 0
            answer += " "
        elif not count % 2:
            i = ord(i)
            if i >= 97:
                i = i - 32
            answer += chr(i)
            count += 1
        else:
            i = ord(i)
            if i <= 90:
                i = i + 32
            answer += chr(i)
            count += 1
    return answer


print(solution(s))
