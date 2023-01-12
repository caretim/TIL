# 무게당 기대치 정렬 -> 무게 체크하며 가방에 담기

# 무게가 낮고 ->가치가 높은 순으로 람다정렬 후
# 순차적으로 가방에 담기 -> 실패 다른 조합으로도 더 높은 점수가 나올 수 있음 그냥 컴바인사용 ? 무게 이내일때 점수를 리스트에 담고 프린트?


n, max_w = map(int, input().split())

items = []

for __ in range(n):
    w, v = map(int, input().split())
    av = v / w
    items.append((av, w, v))


items.sort(key=lambda x: (-x[0], x[1], x))

print(items)

result = 0
backpack = 0

for av, w, v in items:
    if w + backpack <= max_w:
        result += v
        backpack += w

print(result)
