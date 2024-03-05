import sys

input = sys.stdin.readline
case = 0
while True:
    
    N = int(input())
    if N == 0:
        break
    case += 1
    manito = dict()
    for _ in range(N):
        FROM, TO = map(str, input().split())
        manito[FROM] = TO
    
    count = 0
    while manito:
        origin = next(iter(manito))
        start = origin
        end = manito.get(start)
        manito.pop(start)
        # print(manito)
        while end in manito.keys():
            start = end
            end = manito.get(start)
            if end == origin:
                count += 1
                # print(count, end = ' ')
            manito.pop(start)
    print(case, count)