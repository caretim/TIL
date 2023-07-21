table = [0 for __ in range(491)]


table[1]=1

for i in range(2,491):
    table[i] = table[i-1]+table[i-2]

while True:
    h= int(input())
    if h == -1:
        break
    print(f'Hour {h}: {table[h]} cow(s) affected')