
numbers =[1, 2, 100, -99, 1, 2, 3]

def double(n):
    return(n*2)
def solution(numbers):
    answer = list(map(double,numbers))
    return answer
print(solution(numbers))