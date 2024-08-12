
import sys

input = sys.stdin.readline

x, y, w ,s = map(int,input().split())

reuslt = 0
if w > s:
    reuslt += min(x,y)*s
    left = abs(x-y)
    reuslt += (left//2*2)*s
    left -= (left//2*2)
    reuslt += left*w
elif 2*w > s:
    reuslt += min(x,y)*s
    left = abs(x-y)
    reuslt += left*w
else:
    reuslt = (x+y)*w
print(reuslt)