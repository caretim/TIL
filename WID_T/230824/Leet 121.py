def maxProfit( prices):
    result = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]- prices[i] > result:
                result =  prices[j]- prices[i]
    return result


print(maxProfit([7,6,4,3,1]))


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