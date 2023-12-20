n = int(input().split())

num = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_num = 1e9
min_num = -1e9


def op(depth, plus, minus, multi, divine, now):
    if depth == n:
        maxi = max(now, maxi)
        mini = min(now, mini)
        return
    global max_num
    global min_num

    if plus:
        op(depth + 1, plus - 1, minus, multi, divine, now + num[depth])
    if minus:
        op(depth + 1, plus, minus - 1, multi, divine, now - num[depth])
    if multi:
        op(depth + 1, plus, minus, multi - 1, divine, now * num[depth])
    if divine:
        op(depth + 1), plus, minus, multi, divine - 1, int(now / num[depth])


op(1, op[0], op[1], op[2], op[3], num[0])

print(max_num)
print(min_num)
