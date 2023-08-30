nums = [1,3,5,6]

target = 5

# def searchInsert(nums, target):
#     left =0
#     right = len(nums)-1
#     while left<=right:
#         mid = (left+right)//2
#         if nums[mid] == target:
#             return mid
#         if nums[mid]>target:
#             left=mid+1
#         elif nums[mid]>target:

        

def searchInsert(nums, target):
        left =0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] == target:
                print(mid)
                return mid
            elif nums[right] ==target:
                return right
            elif nums[left]== target:
                return left
            if nums[mid]<target:
                right=mid-1
            else:
                left=mid+1

print(searchInsert(nums,target))