def solution(rsp):
    answer = ""
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
        print(i)
    return answer


rsp = "205"
print(solution(rsp))
