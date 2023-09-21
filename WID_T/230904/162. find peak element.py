class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)<1:
            return 0
        left =0
        right = len(nums)-1
        while left<right-1: #왼쪽 포인터가 오른쪽 포인터를 넘는 순간 while문 중지
            mid = (left+right)/2 #중간값을 기준으로 양 옆 비교 조건 만족시 return 
            if nums[mid] >nums[mid+1] and nums[mid]<nums[mid-1]:
                return mid
            if nums[mid]<nums[mid+1]: #본인 인덱스 앞쪽이 본인의 수보다 크다면 왼쪽조건 충족
                left = mid+1
            else:
                right =mid-1 
        return left 

        """
        :type nums: List[int]
        :rtype: int
        """
        