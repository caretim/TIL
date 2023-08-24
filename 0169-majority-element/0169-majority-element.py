class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n]+=1

        return (max(dict,key=dict.get))
