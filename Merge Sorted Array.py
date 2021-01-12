class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        for i in range(len(nums1)):
            if nums1[i]==0 and nums1[i:].count(0)==len(nums2):
                nums1[i]=nums2[0]
                nums2.pop(0)
            else:
                continue
        nums1.sort()
        
        
        
        
