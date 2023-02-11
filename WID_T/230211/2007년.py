# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다.
# 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.


# 2007년

date_m = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334,
}

m, d = map(int, input().split())


result = (date_m[m] + d) % 7


if result == 1:
    print("MON")

elif result == 2:
    print("TUE")

elif result == 3:
    print("WED")

elif result == 4:
    print("THU")

elif result == 5:
    print("FRI")

elif result == 6:
    print("SAT")

elif result == 0:
    print("SUN")
