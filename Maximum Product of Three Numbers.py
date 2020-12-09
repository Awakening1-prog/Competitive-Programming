class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        l.append(nums[-1]*nums[-2]*nums[-3])
        l.append(nums[0]*nums[1]*nums[-1])
        return max(l)