
array=[1, 5, 2, 6, 3, 7, 4]	
commands= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for i,j,k in commands:
        new = array[i-1:j]
        new.sort()
        print(array)
        print(new,"자른배열")
        answer.append(new[k-1])
        print(new[k-1])
    return answer


print(solution(array,commands))