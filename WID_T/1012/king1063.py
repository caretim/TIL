n = 8
k, s, sq = input().split()


move = {  # 입력시 킹의 움직임
    "RT": (1, 1),
    "T": (1, 0),
    "LT": (1, -1),
    "L": (0, -1),
    "R": (0, 1),
    "LB": (-1, -1),
    "B": (-1, 0),
    "RB": (-1, 1),
}

# ord와 int로 변환해주는 이유
# 받는 A - H까지의 알파벳을 숫자로 전환해준 후 좌표값으로 변환한다.
# 매트릭스를 사용하지않고 단순 숫자계산으로 풀었기에 좌표의 0값을 생각해서
# 1을 더 빼주어서 1의 값을 좌표 0으로 상정해준다.
kx = ord(k[0]) - 65
ky = int(k[1]) - 1
sx = ord(s[0]) - 65
sy = int(s[1]) - 1


for p in range(int(sq)):

    mo = move.get(input())  # 움직임 입력시 딕셔너리에서 입력에 맞는 키의 밸류를 가져온다.
    kmy = ky + mo[0]
    kmx = kx + mo[1]  # Y축과 X축에 더 해준다.

    if (
        0 > kmy or kmy >= 8 or 0 > kmx or kmx >= 8
    ):  # 더 해준 값이 좌표 0보다 작거나 8보다 크다면 범위를 벗어나므로 continue를 통해 다음 반복순서로 넘어간다.
        continue
    elif 0 <= kmy or kmy < 8 or 0 <= kmx or kmx < 8:  # 0보다 같거나 크고 8보다 작다면 아래의 코드를 시행한다.
        if kmy == sy and kmx == sx:  # 만일 킹의 위치와 돌의 위치가 같다면 돌을 진행 방향으로 밀어준다.
            smy = sy + mo[0]
            smx = sx + mo[1]
            if (
                0 > smy or smy >= n or 0 > smx or smx >= n
            ):  # 이때 32번줄의 if문과 같이 범위를 벗어나는지 확인한다.
                continue
            elif (
                0 <= smy or smy < 8 or 0 <= smx or smx < 8
            ):  # 범위 내에서 시행이 가능하다면 위에서 29,30번줄, 36,37번줄에 적어둔 코드대로 위치를 이동한다.
                sy = smy
                sx = smx
                ky = kmy
                kx = kmx
        else:  # 돌의 위치와 킹의 위치가 다르다면 변경해준 위치 그대로 이동한다.
            ky = kmy
            kx = kmx
# 체스판의 y 축의 위치가 반전되어있으므로 이를 고려해서 반전된 위치로 보내준다.
print(chr(kx + 65), ky + 1, sep="")
print(chr(sx + 65), sy + 1, sep="")
