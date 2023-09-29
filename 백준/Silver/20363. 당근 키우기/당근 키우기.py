
import math

x, y = map(int, input().split())  

print(math.trunc(x + y + (min(x, y) / 10))) 