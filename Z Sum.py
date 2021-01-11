class Solution:
    def solve(self, matrix):
        res=0
        res+=sum(matrix[0])+sum(matrix[-1])
        i=len(matrix)-2
        j=1
        while j<len(matrix)-1:
            print(matrix[j][i])
            res+=matrix[j][i]
            i-=1
            j+=1
        return res
