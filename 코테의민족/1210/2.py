# https://school.programmers.co.kr/learn/courses/30/lessons/120842



def solution(num_list, n):

    answer = []
    append_list=[]
    count=0
    for k in num_list:
        count+=1
        append_list.append(k)
        if count%n==0:
            print(append_list)
            answer.append(append_list)
            append_list=[]
        
    return answer

a= [1,2,3,4,5,6,7,8,9]
n= 3

print(solution(a,n))
