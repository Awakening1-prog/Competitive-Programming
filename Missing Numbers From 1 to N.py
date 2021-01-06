


class Solution:
    def solve(self, nums):
        dp=[0]*(len(nums)+1)
        for i in nums:
            dp[i]+=1
        l=[]
        for i in range(1,len(dp)):
            if dp[i]==0:
                l.append(i)
        return l
