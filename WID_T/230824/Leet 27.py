class Solution(object):
    def removeElement(self, nums, val):
        cnt = 0
        move =0 
        num_count = len(nums)-1
        while move <= num_count:
            changeNum= nums[num_count]
            if nums[move]== val :
                nums[num_count] = nums[move] 
                nums[move] = changeNum
                num_count-=1 
                cnt+=1
            else:
                move+=1
        for __ in range(cnt):
            nums.pop()

class Solution(object):
    def removeElement(self, nums, val):
        cnt = 0 #숫자의 카운트 
        move =0 
        num_count = len(nums)-1
        while move <= num_count:
            changeNum= nums[num_count]
            if nums[move]== val :
                nums[num_count] = nums[move] 
                nums[move] = changeNum
                num_count-=1 
                cnt+=1
            else:
                move+=1
        for __ in range(cnt):
            nums.pop()



Solution.removeElement([3,2,2,3],3)

