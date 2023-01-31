# 왼손 1,4,7 오른손 3,6,9 가운데 2,5,8,0 은 가까운 손가락을 사용
# but 거리가 가까울때는 왼손잡이는 왼손 오른손은 오른손 사용

pad = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2],
    "0": [3, 1],
    "*": [3, 0],
    "#": [3, 2],
}
# count=1
# row=0
# for k in range(1,10):
#     if count>3:
#         count=1
#         row+=1
#     if count==1:

# 절대값으로 비교 후 값이 같다면 ? 손잡이에 따라 움직이자,
# 딕셔너리? 이중리스트?


def solution(numbers, hand):
    answer = ""
    ly, lx = 3, 0
    ry, rx = 3, 2
    left = [1, 4, 7]
    right = [3, 6, 9]
    center = [2, 5, 8, 0]
    for k in numbers:
        if k in right:
            answer += "R"
            k = str(k)
            ry, rx = pad[k][0], pad[k][1]
        elif k in left:
            k = str(k)
            answer += "L"
            ly, lx = pad[k][0], pad[k][1]
        elif k in center:
            k = str(k)
            cy, cx = pad[k][0], pad[k][1]
            Left_range = abs(cy - ly) + abs(cx - lx)
            right_range = abs(cy - ry) + abs(cx - rx)
            if Left_range == right_range:
                print(Left_range, right_range)
                print(ly, lx, ry, rx, cy, cx, k, "거리가같을때")
                if hand == "right":
                    answer += "R"
                    ry, rx = cy, cx
                else:
                    answer += "L"
                    ly, lx = ly, lx

            elif Left_range < right_range:
                answer += "L"
                print(ly, lx, ry, rx, cy, cx, k)
                ly, lx = cy, cx
            elif Left_range > right_range:
                answer += "R"
                print(ly, lx, ry, rx, cy, cx, k)
                ry, rx = cy, cx

    return answer


numbers = [7, 0, 8, 2, 8]
hand = "left"

print(solution(numbers, hand))

# 정답="LRLLR"
# 오답="LRLLL"
# 왼= 0,1
# 오 = 3,1
# 8 = 3,1
