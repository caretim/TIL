# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.


n= int(input())


card_counter={}

for __ in range(n):
    card= int(input())
    if card not in card_counter:
        card_counter[card]= 1
    else:
        card_counter[card]+= 1


mc=max(card_counter.values())

# 값 내림차순순정렬 -> 키 오름차순정렬 
max_card=[]

for r in card_counter:
    if card_counter[r] == mc:
        max_card.append(r)

max_card.sort(reverse=False)

print(max_card[0])