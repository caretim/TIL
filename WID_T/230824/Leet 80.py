nums = [0,0,1,1,1,1,2,3,3]


cnt = 1
index =0

for i in range(1,len(nums)):
    if nums[i] != nums[index]:
        cnt=1
        index+=1
        nums[index]=nums[i]
    elif nums[i] == nums[index]:
        if cnt <2:
            cnt+=1
            index+=1
            nums[index]=nums[i]



print(cnt)
print(nums)
