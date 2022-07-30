
T = int(input())

for test_case in range(1, T + 1):
        
    n= input()

    numbers= []

    acn ='3','4','5','6','9'

    for nums in n:
        if nums=='-':
            continue
        else :
            numbers.append(nums)

    if numbers[0] in acn and len(numbers) == 16:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
