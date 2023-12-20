import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    
    count = 0
    
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        
        d1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        d2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
        
        if d1 < r and d2 > r:
            count += 1
        elif d2 < r and d1 > r:
            count += 1
            
    print(count)