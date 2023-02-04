
import sys
sys.stdin = open("_괄호짝짓기.txt")

T = 10

for test_case in range(1, T + 1):

    n= int(input())

    vsp= input()

    vsls = []

    swi = 1
    for i in vsp:
        if i == '(':
            vsls.append(i)
        elif i == '[':
            vsls.append(i)
        elif i == '<':
            vsls.append(i)
        elif i == '{':
            vsls.append(i)

        elif i == ')':
            if len(vsls) == 0 or vsls.pop() != '(':
                swi = 0
        elif i == ']':
            if len(vsls) == 0 or vsls.pop() != '[' :
                    swi = 0
        elif i == '>':
            if len(vsls) == 0 or vsls.pop() != '<':
                swi = 0
        elif i == '}':
            if len(vsls) == 0 or vsls.pop() != '{':
                swi = 0


    print(f'#{test_case} {swi}')