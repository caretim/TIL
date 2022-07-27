# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 두 정수를 문자열로 받은 뒤 역순으로 배열하고 
#역배열한 값을 정수로 int로 형변환하여 숫자를 비교하고 큰 값을 출력한다,

# n1,n2 =input().split()

sn1= n1[::-1]
sn2= n2[::-1]
in1=int(sn1)
in2=int(sn2)
print(max(in1,in2))



