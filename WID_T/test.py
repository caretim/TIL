a = input()
b = input()
 
number = ""

for i in range(len(a)):
    number += a[i]
    number += b[i]
 
result = number


 
while len(result) != 2:
    num = []
    for i in range(len(result)-1):
       new_num = (int(result[i])+int(result[i+1]))%10
       num.append(str(new_num))
    result=num


print(*result,sep='')

#10-3619-5974 이면, 7346715995393764에서 시작하여 070386484822030, 77314022204233, 4045424424656, 449966866011, 83852442612, 1137686873, 240344450, 64378895, 0705674, 775131, 42644, 6808, 488, 26