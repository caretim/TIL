# > 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# > 

# ### 오류 코드


# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)


# ### Output
# {'Apricot': 1,
#  'Blackcurrant': 1,
#  'Cantaloupe': 1,
#  'Feijoa': 1,
#  'Grapefruit': 1,
#  'Juniper berry': 1,
#  'Salal berry': 1,
#  'Soursop': 1}


from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
        #변수를 추가해주는게 아니라 요소를 전체를 하나의 값으로 바꿔주며 
        # 반복됨 변수가 누적 저장되게 만들자
        #fruit_count = {fruit: 1} ->변수를 오른쪽의 값으로 지정 (더해주는게아님)
        #fruit_count[fruit] = 1 -> fruit count에 fruit이라는 키의 값에 1로 지정해서 넣는다
    else:
        fruit_count[fruit] += 1 # 다른경우count딕셔너리에 이미 있을경우 값을 플러스 1 해준다.

pprint(fruit_count)