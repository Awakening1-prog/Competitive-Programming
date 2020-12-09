class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        nums=nums[::-1]
        if len(nums)<3:
            return max(nums)
        else:
            return nums[2]