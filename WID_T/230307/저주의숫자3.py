def solution(n):
    num=[]
    for i in range(0,200):
        ic= str(i)
        if i%3 !=0 and '3' not in ic:
            num.append(i)     
    answer = num[n]
    print(num)
    return answer

print(solution(int(input()))) 
