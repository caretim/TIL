import sys

input =sys.stdin.readline

def solution(scores):
    result = 0
    max_rank = [100001, 100001]
    for score in sorted(scores):
        if max_rank[1] > score[1]:
            max_rank = score
            result += 1
    return result



for _ in range(int(input())):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    print(solution(scores))