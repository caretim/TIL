alpha = input().strip()

def solv():
    answer_list = [alpha]
    answer = alpha
    for _ in range(len(answer)):
        tmp1 = list(answer)
        tmp2 = list(answer)
        target_idx = -1
        for idx in range(len(answer)):
            if target_idx == -1:
                tmp1[idx] = ''
                target_idx = idx
            else:
                tmp2[idx] = ''
                str_tmp1,str_tmp2 = ''.join(tmp1),''.join(tmp2)
                if sorted((str_tmp1, str_tmp2))[0] == str_tmp2:
                    tmp1[target_idx] = answer[target_idx]
                    tmp1[idx] = ''
                    target_idx = idx
                tmp2[idx] = answer[idx]
        answer = ''.join(tmp1)
        answer_list.append(answer)
    answer_list.reverse()
    for ans in answer_list[1:]:
        print(ans)
solv()