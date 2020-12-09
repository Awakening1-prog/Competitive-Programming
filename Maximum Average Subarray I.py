class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=-1000000000000
        s1=0
        if len(nums)==1:
            return nums[0]
        d=collections.deque()
        for i in range(k):
            s1+=nums[i]
        s1=s1/k
        s=max(s,s1)
        #print(s)
        for i in range(1,len(nums)-k+1):
            #print(nums[i+k-1])
            s1=s1-(nums[i-1]/k)+((nums[i+k-1])/k)
           # print(s)
            s=max(s,s1)
        return s
            