def solution(num, total):
    answer = []
    pointer = total//num
    
    #num의 개수만큼 나눠지는 경우  
    #홀수 일 경우 total / num지점 1 앞뒤로 대칭의 수 
    #짝수 일 경우 
    k= pointer - num//2
    if not num % 2 :
        k+=1
    for i in range(k,k+num):
        answer.append(i)
    return answer