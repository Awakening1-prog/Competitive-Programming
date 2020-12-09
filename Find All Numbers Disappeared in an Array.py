class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        if len(nums)==0:
            return 
        nums1=set(nums)
        a=len(nums)
        for i in range(1,a+1):
            if i not in nums1:
                l.append(i)
        return l