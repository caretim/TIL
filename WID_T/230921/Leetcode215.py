import heapq
def changeMinus(n):
        return -n
class Solution(object):
    def findKthLargest(self, nums, k):
        result = 0
        q= []
        for i in nums:
            heapq.heappush(q,-i)

        for __  in range(k):
            result = heapq.heappop(q)
        return -result