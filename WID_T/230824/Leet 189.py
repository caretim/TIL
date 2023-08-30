def rotate(nums, k):
    if len(nums)!=1 and k !=0:
        
        len_num= len(nums)
        k = k%len_num
        nums [:]= nums[-k:] + nums[:len_num-k]
        
        print(nums)

rotate([1,2,3,4,5,6,7],k = 3)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_num= len(nums)
        k= k%len_num
        result = nums[-k:] + nums[:-k]
        nums.clear()
        for i in result:
            nums.append(i)