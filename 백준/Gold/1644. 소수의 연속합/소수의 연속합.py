import sys 

input =sys.stdin.readline

n= int(input())

sq_n = int(n**(0.5))
temp = [1] * (n + 1)
for i in range(2, sq_n+1):
    if temp[i] == 1:
        for j in range(i*2, n+1, i):
            temp[j] = 0
num_list = [i for i in range(2, n+1) if temp[i] == 1]


result = 0

start = 0
end = 0
while end < len(num_list):
    if sum(num_list[start:end+1]) ==n:
        result += 1
        end += 1
    elif sum(num_list[start:end+1]) >n:
        start += 1
    elif sum(num_list[start:end+1]) <n:
        end += 1
print(result)


