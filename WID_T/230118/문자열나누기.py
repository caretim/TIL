# def solution(s):
#     answer = 0
#     while s:
#         print(s)
#         first = s[0]
#         same = 0
#         difer = 0
#         for i in range(len(s)):
#             if s[i] == first:
#                 same += 1
#             else:
#                 difer += 1
#             if same == difer:
#                 s = s[(i + 1 - len(s)) :]
#                 break
#         answer += 1
#         if len(s) <= 2:
#             break

#     return answer + 1


def solution(s):
    answer = 0
    while True:
        print(1)
        d_char = ""
        first = s[0]

        same = 0
        difer = 0
        for i in range(len(s)):
            if s[i] == first:
                same += 1
            else:
                difer += 1
            d_char += s[i]
            if same == difer:
                print(same, difer, d_char, s)
                s = s.lstrip(d_char)
                answer += 1
                print(s)
                break
        if len(s) <= 2:
            break
    return answer + 1


s = "aaabbaccccabba"


print(solution(s))
