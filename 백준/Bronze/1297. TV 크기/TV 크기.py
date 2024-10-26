import sys

input =sys.stdin.readline



#대각선의 길이 , h,w 높이 너비 비율 

# 피타고라스의 정리 대각선 제곱 값은 너비제곱,높이제곱의 합과 같음
# 대각선 제곱/h+w 

d,h,w =map(int,input().split())



sq = (d**2/((h**2)+(w**2)))**(1/2)


print(int(h*sq),int(w*sq))


