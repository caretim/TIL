# > 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. ****
# > 

#Input

# 123


# Output
#6

# 슬라이싱을 통해 더해주면 된다. 슬라이싱되는 숫자를 바로 더할지 아니면 리스트에 추가했다가
# 다시 넣을건지 ?  형변환을 통해 위치 측정 밑 더해주기? 
#슬라이싱 
n = (int(input()))

str_n = str(n)


nsum= 0

for i in range(len(str_n)):
    # print (n[i:i+1],type(i))
    f = int(str_n[i:i+1])
    nsum += f
    

print (nsum)

#while문으로 나누기 10해서 구해보기


n = int(input())
a= []
b= 0
count= 0
while n != 0 :
    a.append(n%10) #n을 10으로 나눈 나머지를 a리스트에 넣는다
    n= n//10       #n은 10으로 나눠준 몫을 순환시킨다.
    count +=1      #n 카운팅을 통해 숫자의 자리수를 계산해준다
    # if n <1:
    #     break

for i in a: # 카운팅에 저장된 번호로 리스트 인덱스를 불러온다. 
    b += i 

print(b)
