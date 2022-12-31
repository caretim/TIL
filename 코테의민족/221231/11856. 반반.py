n= int(input())


for test_case in range(1,n+1):
    check=0
    arr = list(input())
    set_arr = set(arr)
    list_arr = list(set_arr)
    if len(set_arr) !=2:
        check=1
    else:
        result=[0,0]

        for i in arr:
            if i==list_arr[0]:
                    result[0]+=1
            elif i==list_arr[1]:
                    result[1]+=1
        for k in result:
            if k != 2:
                check=1
    if check == 0:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
