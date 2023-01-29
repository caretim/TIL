n, k = map(int, input().split())

result = []

stack = [i for i in range(1, n + 1)]

count = 1

# 와일안에 포문으로 반복적으로 stack갯수만큼 순환
# 커서를 만든 후 카운트 커서를 만든다.
# 포문이 끝난 후 결과에 넣은 값의 인덱스를 삭제
# 다시 시행
while stack:
    del_list = []
    for p in range(len(stack)):
        if count == k:
            result.append(str(stack[p]))
            del_list.append(stack[p])
            count = 1
        else:
            count += 1
    for i in del_list:
        stack.remove(i)

# ^^ 갱장히 화가나따.. 띄어쓰기 붙여줘야했던거냐고 ㅠㅠ 
print("<", ", ".join(result), ">", sep="")
