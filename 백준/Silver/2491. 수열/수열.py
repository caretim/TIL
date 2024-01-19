n = int(input())

nums = list(map(int, input().split()))


result = []


def check_nums(numList):
    max_list = 0
    checklist = []
    checklist.append(numList[0])
    now = numList[0]
    for i in range(1, len(numList)):
        if now <= numList[i]:
            checklist.append(numList[i])
            now = numList[i]
        else:
            max_list = max(len(checklist), max_list)
            checklist = [numList[i]]
            now = numList[i]
    max_list = max(len(checklist), max_list)
    return max_list


print(max(check_nums(nums), check_nums(nums[::-1])))
