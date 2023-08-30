import queue
target = 15
nums = [5,1,3,5,10,7,4,9,2,8]

min_range=1e9


for i in range(len(nums)):  #인덱스
    for ii in range(i,-1,-1):
        print(ii,nums[-(ii+1):])
        if target <=sum(nums[-(ii+1):]):
            min_range= min(min_range,ii+1)
            a= nums[-(ii+1):]

print(a)

print(min_range)



# left =0



# class Solution(object):
#     def minSubArrayLen(self,s, nums):
#         res = maxsize
#         left, total = 0, 0
        
#         for i in range(len(nums)):
#             total += nums[i]
#             while total >= s:
#                 res = min(res, i - left + 1)
#                 total -= nums[left]
#                 left += 1
        
#         return res if res != maxsize else 0