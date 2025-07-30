class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]>target:
                    break
                elif matrix[i][j]==target:
                    return True
        return False
        