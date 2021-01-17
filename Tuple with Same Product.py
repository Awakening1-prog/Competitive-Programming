class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h=defaultdict(int)
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x=nums[i]*nums[j]
                res+=h[x]
                h[x]+=1
        return 8*res
                
            
