class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self,A):
        i=-1
        j=-1
        res=0
        c=0
        h={}
        while True:
            f1=0
            f2=0
            while i<len(A)-1:
                i+=1
                f1=1
                if A[i] not in h:
                    h[A[i]]=1
                else:
                    h[A[i]]+=1
                if h[A[i]]>=2:
                    break
                else:
                    res=max(res,abs(i-j))
            while j<i:
                j+=1
                f2=1
                h[A[j]]-=1
                if h[A[j]]==1:
                    res=max(res,abs(i-j))
                    break
            if f1==0 and f2==0:
                break
        return res
