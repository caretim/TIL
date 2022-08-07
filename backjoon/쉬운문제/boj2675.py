

for tc in range(int(input())):

    a,b = input().split()

    result= []
    for r in b:
        for __ in range(int(a)):
            result.append(r) 


    print(''.join(result))