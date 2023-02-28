def solution(s):
    answer = []
    dic = {}
    # for k in range(97,123):
    #     dic[chr(k)]=0   
    print(dic)
    for i in range(len(s)):
        ch = s[i]
        if ch not in dic:
            dic[ch]=0
            answer.append(-1)
            dic[ch]=i
        else:
            answer.append(i-dic[ch])
            dic[ch]=i           

    return answer
solution(['b','a','b','a','b','a'])
