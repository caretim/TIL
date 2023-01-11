for tc in range(int(input())):
    n = int(input())

    # 1= 1 ,2=2 ,3=4,4=7,5=13,6=24
    # 점화식 dp[i]= dp[i-1]+dp[i-2]+dp[i-3]

    dp = [1, 2, 4]  # 0번인덱스가 숫자 1일때부터 시작

    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[n - 1])  # 0번인덱스가 숫자1의 123더하기합임 그러므로 0-1
