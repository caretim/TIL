import sys
import heapq

input = sys.stdin.readline

n = int(input())

class_list = [tuple(map(int, input().split())) for _ in range(n)]
class_list.sort()

room = []
for s, t in class_list:

    if len(room) == 0:
        room.append(t)
        continue

    end_class = room[0]
    if end_class <= s:
        heapq.heappop(room)

    heapq.heappush(room, t)

result = len(room)
print(result)
