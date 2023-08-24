class Solution(object):
    def removeDuplicates(self, nums):
        set_nums = set(nums)
        for __ in range(len(nums)):
            nums.pop()
        for i in set_nums:
            nums.append(i)
        nums.sort()

        """
        :type nums: List[int]
        :rtype: int
        """