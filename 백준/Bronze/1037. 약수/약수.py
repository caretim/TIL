n= int(input())

num_list = list(map(int,input().split()))


num_list.sort()

print(num_list[0]*num_list[-1])



# count=2
# while True:
#     max_n= max(num_list)
#     r = max_n*count
    