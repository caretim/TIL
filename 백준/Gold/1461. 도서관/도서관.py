n, m = map(int, input().split())

book = list(map(int, input().split()))

M_list = []

P_list = []
result = 0
if len(book) == 0:
    print(0)
    exit()
elif len(book) == 1:
    print(book[0])
    exit()


def move(books, m):
    distant = 0
    for i in range(m):
        try:
            if i == 0:
                distant = books.pop()
            else:
                books.pop()
        except:
            break

    return distant


for i in book:
    if 0 < i:
        P_list.append(i)
    else:
        M_list.append(-i)
P_list.append(0)
M_list.append(0)


P_list.sort()
M_list.sort()


if max(M_list) <= max(P_list):
    result += move(P_list, m)
else:
    result += move(M_list, m)


while P_list:
    result += move(P_list, m) * 2

while M_list:
    result += move(M_list, m) * 2


print(result)
