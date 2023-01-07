my_string ="3 + 4"





def solution(my_string):
    k= my_string.split()
    answer = int(k[0])
    print(k)
    for j in range(len(k)):
        if j%2==1:
            if k[j]=='+':
                answer+=int(k[j+1])
            else: 
                answer-=int(k[j+1])
        print(answer)
    return answer



print(solution(my_string))

