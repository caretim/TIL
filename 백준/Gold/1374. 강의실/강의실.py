n = int(input())


s_dict = {}
e_dict = {}

time = set()
for __ in range(n):
    k, s, e = map(int, input().split())
    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1

    if e not in e_dict:
        e_dict[e] = 1
    else:
        e_dict[e] += 1
    time.add(s)
    time.add(e)

time = list(time)
time.sort()


now = 0
result = 0
for i in time:
    if i in s_dict:
        now += s_dict[i]
    if i in e_dict:
        now -= e_dict[i]
    if result < now:
        result = now


print(result)
