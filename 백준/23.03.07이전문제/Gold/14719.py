# 오른쪽으로 진행하며 큰 수가 나올때 갱신 ,
# 더 큰수가 나오거나 벽을 만났을때 그 사이의 인덱스 값들을 계산해줌
# 계산 후에 오른쪽으로 더 진행 할 수 있다면 계속해서 진행
# 첫 벽 가지고 진행, 벽은 클때, 만일 작다면 리스트에 담아둠 크거나 같은벽만나면
# 담아둔 리스트의 값들을 계산해서 워터변수에 저장
# 그냥 배열 넣고 x축으로 계산해주자
# 중간에 작은수나오면 변수 하나씩 넣기 귀찮음

h, w = map(int, input().split())


matrix = [[1] * w for _ in range(h)]

arr = list(map(int, input().split()))

water = 0
# 빈공간채워넣기
for x in range(w):
    for y in range((h - arr[x])):
        matrix[y][x] = 0
# 가로축 기준으로 빗물 계산
for y in range(h):
    find_space = 0
    add_water = 0
    for x in range(w):
        if matrix[y][x] == 1:  # 벽 찾았을때,쌓였던 빗물 축적
            water += add_water
            add_water = 0
            find_space = 1
        if matrix[y][x] == 0 and find_space == 1:
            add_water += 1
print(water)


# for k in matrix:
#     print(k)
