from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",

]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = fruit_count+{fruit: 1}   #변수를 추가해주는게 아니라 내부의 요소만 바꿔주는중.
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)


fruit_count = {}
for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}


print(fruit_count)