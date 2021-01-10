class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack=[]
        l=[]
        for i in range(len(A)):
            while stack and stack[-1]>=A[i]:
               stack.pop()
            if stack==[]:
                l.append(-1)
            else:
                l.append(stack[-1])
            stack.append(A[i])
        return l
