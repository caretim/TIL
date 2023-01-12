# 1 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
# 2 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
# 3 현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
# 4 현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

n = int(input())

channels = []

result = []
for __ in range(n):
    channels.append(input())

count = 0
for c in range(len(channels)):
    if channels[c] == "KBS1" or "KBS2":
        if channels[c] == "KBS1":
            for i in range(c - 1):
                result.append(1)
