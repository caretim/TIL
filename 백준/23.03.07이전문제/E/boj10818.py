# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

from posixpath import split


t = int(input())

nums =(map(int,input().split()))

lis= []

for i in nums:
    lis.append(i)

# nums.append(map(int,input().split()))

print(min(lis),max(lis),sep=(' '))
