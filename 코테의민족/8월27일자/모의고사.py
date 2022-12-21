
a_num_lsit = [1,2,3,4,5]
b_num_list = [1,3,4,5]
c_num_list = [3,1,2,4,5]

def a_list(i):
    return_list = []
    for j in range(1,i+1):        
        return_list.append(a_num_lsit[((j%5)-1)])
    return return_list


def b_list(i):
    cnt = 0
    return_list = []
    for j in range(1,i+1):
        if j%2 == 0:
            return_list.append(b_num_list[cnt])
            cnt+=1
            if cnt ==4:
                cnt=0
        else:
            return_list.append(2)
    return return_list
        
def c_list(i):
    return_list=[]
    for j in range(1,i+1):
        k = j%10 
        if k == 1 or k == 2:
            return_list.append(3)
        elif k == 3 or k == 4:
            return_list.append(1)
        elif k == 5 or k == 6:
            return_list.append(2)
        elif k == 7 or k == 8:
            return_list.append(4)
        elif k == 9 or k == 0:
            return_list.append(5)
    return return_list


def solution(answers):
    n = len(answers)
    a = a_list(n)
    b = b_list(n)
    c = c_list(n)
    score_list=[0,0,0]
    for r in range(n):
        re = answers[r]
        if a[r] == re:
            score_list[0]+=1
        if b[r] == re:
            score_list[1]+=1
        if c[r] == re:
            score_list[2]+=1
    high = max(score_list)

    result=[]
    for num in range(1,4):
        if score_list[num-1] == high:
            result.append(num)
    result.sort()
    print(a,b,c)
  
    return result

answers = [1,3,2,4,2]
print(solution(answers))



    
    
