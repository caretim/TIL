for tc in range(int(input())):
    n, m = map(int, input().split())
    dp = [0, 1]
    check1 = 1
    check2 = 1
    count = 1
    for i in range(2, 1000001):  # 범위는 최대로 잡아준다 브레이크로 멈출거라ㄱㅊ
        dp.append((dp[i - 1] + dp[i - 2]) % m)
        check1 = check2
        check2 = dp[i]
        if (
            check1 == 0 and check2 == 1
        ):  # 피사노주기의 시작인 0,1로 구분 체크1과 2에 인덱스 값을 넣어서 0,1이라면 주기 새로 시작
            print(n, count)
            break
        else:
            count += 1
