class Solution:
    def solve(self, n):
        l=[1,2]
        c=3
        while l[-1]<n:
            l.append(factorial(c))
            c+=1
        if l[-1]>n:
            l.pop()
        for i in range(len(l)-1,-1,-1):
            if l[i]<=n:
                n-=l[i]
        return n==0
