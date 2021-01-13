class Solution:
    def distinctSubseqII(self, S: str) -> int:
        c=0
        h={}
        dp=[0]*(len(S)+1)
        dp[0]=1
        for i in range(1,len(S)+1):
            dp[i]=2*dp[i-1]
            if S[i-1] in h:
                print(h[S[i-1]])
                dp[i]=dp[i]-dp[h[S[i-1]]]
            h[S[i-1]]=i-1
        #print(h)
        #print(dp)
        return (dp[-1]-1)%((10**9)+7)
