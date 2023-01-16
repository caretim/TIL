def solution(d, budget):
    d.sort()
    count = 0
    for p in d:
        budget -= p
        if budget < 0:
            break
        else:
            count += 1
    return count
