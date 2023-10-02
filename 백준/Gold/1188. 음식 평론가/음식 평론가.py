
n , m = map(int,input().split())

def gcd(a,b):
    while b:
        a,b = b , a%b
    return a


# print(gcd(n,m))
print(m - gcd(n,m))

#최초의 접근 -> 나눴을 시, 몫이 1이상일 경우와 1이하의 몫일 경우에 조건을 나눠서 계산하시는 방식을 사용했으나 실패,
#문제의 알고리즘 분류에서 유클리드호제법을 보고 공약수를 통해 해결해야한다는 것을 알았다. 
 

    