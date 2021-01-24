class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat)-1):
                for k in range(0,len(mat[0])-1):
                    if mat[j][k]>mat[j+1][k+1]:
                        mat[j][k],mat[j+1][k+1]=mat[j+1][k+1],mat[j][k]
        return mat
