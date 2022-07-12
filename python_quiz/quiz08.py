# numbers = [0, 20, 100]
numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30


min = numbers[0]
lage = 0
second = 0

for i in numbers:
    if min >= i:
        min = i

numbers.remove(-60)

min = numbers[0]
lage = 0
second = 0

for i in numbers:
    if min >= i:
        min = i

print(min)



    
    