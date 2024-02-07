n= int(input())

nums = []

for i in range(n):
    nums.append(int(input()))


nums.sort()



maxcnt =1


for i in range(n-1):
    cnt=1
    if n-5>i:
        for j in range(1,5):
            if nums[i]+4>=nums[i+j]:
                cnt+=1
        if cnt>maxcnt:
            maxcnt=cnt
    else:
        for j in range(1,n-i):
            if nums[i]+4>=nums[i+j]:
                cnt+=1
        if cnt>maxcnt:
            maxcnt=cnt
print(5-maxcnt)
