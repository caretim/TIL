
#1000명의 점수를 나열하여 제일 많이 나온 점수를 출력 
#최빈수가 여러개라면 가장 큰 점수를 출력한다.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_num=input()
    num_list = []
    num_list= list(map(int,input().split()))

    numbers= {}


    for i in num_list:
        if i not in numbers:
            numbers[i] = 1
        else:
            numbers[i] += 1

    maxn=(max(numbers.values()))

    maxnumber=0

    for k,v in numbers.items():
        if v == maxn:
            if maxnumber < k:
                maxnumber= k

    print(f'#{test_case} {maxnumber}')

