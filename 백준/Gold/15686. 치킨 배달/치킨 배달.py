from itertools import combinations

n, m = map(int, input().split())


city = [list(map(int, input().split())) for __ in range(n)]

house = []
chicken = []

result = 1e9



for y in range(n):
    for x in range(n):
        if city[y][x] == 1:
            house.append((y, x))
        elif city[y][x] == 2:
            chicken.append((y, x))

chicken_house = combinations(chicken, m) # 치킨거리의 모든 조합 뽑아냄 


for ch in chicken_house:
    chicken_range=0  # 조합에서의 총 합 치킨거리
    for hy,hx in house: # 하우스에서 치킨거리 ,
        house_range=1e9
        for cy,cx, in ch:
            house_range= min(house_range,(abs(hy-cy)+abs(hx-cx)))
        chicken_range+=house_range # 각 집의 치킨거리를 총 합 치킨거리에 더해줌 
    result = min(result,chicken_range)


print(result)