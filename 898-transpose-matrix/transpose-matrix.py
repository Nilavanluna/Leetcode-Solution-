class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r=len(matrix)
        c=len(matrix[0])
        result=[[0]*r for i in range(c)]
        for i in range(c):
            for j in range(r ):
                result[i][j]=matrix[j][i]
        return result