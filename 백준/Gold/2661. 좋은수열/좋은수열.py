import sys
N = int(input())
choose = []
numbers = [1, 2, 3]

def is_good():
    length = 1
    while True:
        start1, end1 = len(choose) - length, len(choose) - 1
        start2, end2 = start1 - length, start1 - 1

        if start2 < 0:
            break

        if choose[start1:end1 + 1] == choose[start2:end2 + 1]:
            return False

        length += 1

    return True

def choose_num(curr_digit):
    if curr_digit > N:
        for element in choose:
            print(element, end="")
        sys.exit(0)

    for num in numbers:
        choose.append(num)
        if is_good():
            choose_num(curr_digit + 1)
        choose.pop()

choose_num(1)