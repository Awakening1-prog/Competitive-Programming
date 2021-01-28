class Solution:
    def findPairs(self, arr, n): 
        #code here.
        h={}
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j] not in h:
                    h[arr[i]+arr[j]]=1
                else:
                    return 1
        return 0
