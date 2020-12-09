class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c]=nums[i]
                c+=1
        #nums=nums[::-1]
        for i in range(len(nums)-a,len(nums),1):
            nums[i]=0
        return nums
    
       