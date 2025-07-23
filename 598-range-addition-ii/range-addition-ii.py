class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        k=d=99999
        if not ops : 
            return m*n
        for c in ops:
          k=min(c[0],k)
          d=min(c[1],d)
        return k*d
        