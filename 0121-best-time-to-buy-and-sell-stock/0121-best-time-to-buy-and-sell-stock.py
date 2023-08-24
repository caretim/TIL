class Solution(object):
    def maxProfit(self, prices):
        result = 0
        min_value = prices[0]
        for i in prices:
            if i < min_value:
                min_value = i
            if result< i- min_value:
                result = i- min_value
        return result
        """
        :type prices: List[int]
        :rtype: int
        """