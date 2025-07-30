from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
    
        d= defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        r=[]
        for k in range(len(mat)+len(mat[0])-1):
          r += d[k][::-1] if k % 2 == 0 else d[k]  
        return r   