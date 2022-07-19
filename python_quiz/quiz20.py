# > 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. ****
# > 

#Input

# 123


# Output
#6

# 슬라이싱을 통해 더해주면 된다. 슬라이싱되는 숫자를 바로 더할지 아니면 리스트에 추가했다가
# 다시 넣을건지 ?  형변환을 통해 위치 측정 밑 더해주기?

n = (int(input()))

str_n = str(n)

nsum= 0


for i in range(len(str_n)):
    # print (n[i:i+1],type(i))
    f = int(str_n[i:i+1])
    nsum += f
    

print (nsum)

