import itertools 


n,m= map(int,input().split())

num_list= []

for num in range(1,n+1):
    num_list.append(num)


result = list(itertools.combinations_with_replacement(num_list,m))

for r in result:
    print(*r)