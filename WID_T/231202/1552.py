# 일정구간에서 b가 가장 많이 나온곳,
# a와 b중 연달아 나온 횟수 높은 위치에서부터 변경,
# 각 구간별로 count함수를 통해 a 나온 횟수체크?
# -> a의 갯수의 길이만큼 슬라이싱해서 b가 최소로 나오는 구간에서 변경 횟수 지정


def changer(word):
    a_count = word.count("a")
    b_result = 1001
    for i in range(len(word)):
        s, e = i, i + a_count
        if e > len(word):
            e = e - len(word)
            new_word = word[s:] + word[:e]
        else:
            new_word = word[s:e]

        b_count = new_word.count("b")

        if b_result > b_count:
            b_result = b_count
    print(b_result)


word = input()
changer(word)

# print(word[: len(word)])
