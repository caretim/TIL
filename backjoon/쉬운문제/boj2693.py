# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

# 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

import sys
n=int(sys.stdin.readline().rstrip())

for __ in range(n):
    nums =list(map(int,sys.stdin.readline().split()))
    nums.sort()
    print(nums)
    print(nums[7])
