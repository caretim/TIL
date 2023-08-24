class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_num= len(nums)
        k= k%len_num
        result = nums[-k:] + nums[:-k]
        nums.clear()
        for i in result:
            nums.append(i)
        """
        Do not return anything, modify nums in-place instead.
        """