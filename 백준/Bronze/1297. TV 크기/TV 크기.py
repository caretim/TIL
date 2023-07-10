d, h, w = map(int, input().split())
temp = d / ((h ** 2 + w ** 2) ** 0.5) # 대각
H = int(h * temp)
W = int(w * temp)
print(H, W)