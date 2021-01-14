class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        dp=[0]*26
        stack=[]
        l1=[]
        for i in range(len(A)):
            dp[ord(A[i])-ord("a")]+=1
            stack.append(A[i])
            while stack:
                if dp[ord(stack[0])-ord("a")]>1:
                    stack.pop(0)
                else:
                    l1.append(stack[0])
                    break
            if stack==[]:
                l1.append("#")
        return ''.join(l1)
