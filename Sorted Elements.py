class Solution:
    def solve(self, nums):
        l=[]
        for i in nums:
            l.append(i)
        c=0
        l.sort()
        for i in range(len(nums)):
            if nums[i]==l[i]:
                c+=1
        return c
