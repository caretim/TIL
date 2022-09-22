

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    matrix = [list(map(int,input().split())) for __ in range(9)]

    check=1

    for matrix_x in matrix:
        nums =[1,2,3,4,5,6,7,8,9]
        for n in matrix_x:
            if n not in nums:
                check=0
                break
            else:
                nums.remove(n)
                


    for x in range(9):
        nums =[1,2,3,4,5,6,7,8,9]
        for y in range(9):
            if matrix[y][x] not in nums:
                check=0
                break
            else:
                nums.remove(matrix[y][x])

    dy=[-1,-1,-1,0,0,0,1,1,1]
    dx=[-1,0,1,-1,0,1,-1,0,1]



    xy = [1,4,7]
    for y in xy:
        for x in xy:
            nums =[1,2,3,4,5,6,7,8,9]
            for j in range(9):
                ny= y+dy[j]
                nx= x+dx[j]
                if matrix[ny][nx] not in nums:
                    check=0
                    break
                else:
                    nums.remove(matrix[ny][nx])

    print(check)



    print(f'#{test_case} {check}')