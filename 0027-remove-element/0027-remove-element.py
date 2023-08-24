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


        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """