x, y, d, t = map(int, input().split())


# 직사각형의 대각선 길이(피타고라스)

dist = (x**2 + y**2) ** 0.5


print(dist, d)
if t > d:
    print(dist)
    # t가 d보다 작을경우, 직선거리로 이동

else:
    print(t * (dist // d))
    print(dist % d)
    print(min(t * (dist // d) + (dist % d), t * ((dist // d) + 1) + (dist % d)))
    # d범위의 한계치에서 플러스 마이너스 1회 추가,
