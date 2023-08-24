class Solution(object):
    def canJump(self, nums):
        n =len(nums)
        visit = [0] * (n)
        result = False
        q= []

        q.append(0)
        visit[0] = 1
        while q:
            node = q.pop()
            if node == n-1:
                result =True
                break
            for i in range(1,nums[node]+1):
                if node+i <n and visit[i+node] ==0:
                    print(node+i)
                    visit[i+node]=1
                    q.append(node+i)
        return result