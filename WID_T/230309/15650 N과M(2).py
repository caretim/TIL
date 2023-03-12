import itertools 


n,m= map(int,input().split())

num_list= []

for num in range(1,n+1):
    num_list.append(num)


result = list(itertools.combinations_with_replacement(num_list,m))

for r in result:
    print(*r)


# n,m = map(int,input().split())
# arr=[str(i) for i in range(1,n+1)] # 각 번호별로 인덱스 추가 
# print(arr)
# def su(s,index): 
#     if len(s) == m:
#         print(*s)
#         return
#     if index >=n:
#         return

#     su(s+arr[index],index+1)
#     su(s , index + 1)


# su('',0)