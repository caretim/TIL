from itertools import permutations


babbling = ["ayaye"]
ongal = ["aya", "ye", "woo", "ma"]
ongal_list = []
count = 0
for i in range(1, 5):
    for j in permutations(ongal, i):
        print(j)
        ongal_list.append("".join(j))

for b in babbling:
    if b in ongal_list:
        count += 1
