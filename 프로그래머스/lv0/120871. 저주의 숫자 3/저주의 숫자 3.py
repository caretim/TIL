def solution(n):
    num=[]
    for i in range(200):
        ic= str(i)
        if i%3 !=0 and '3' not in ic:
            num.append(i)     
    answer = num[n-1]
    print(num)
    return answer