class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        cs = 0
        rs = 0
        re = len(matrix) - 1
        ce = len(matrix[0]) - 1
        k=0

        while True:
            if cs> ce:
                break
            for i in range(cs, ce + 1):
                k=k+1
                matrix[rs][i]=k  # ✅ rs, not cs

            rs += 1
            if rs > re:
                break

            for j in range(rs, re + 1):
                k=k+1
                matrix[j][ce]=k

            ce -= 1
            if cs > ce:
                break

            for i in range(ce, cs - 1, -1):
                k=k+1
                matrix[re][i]=k

            re -= 1
            if rs > re:  # ✅ Optional guard to avoid over-traversing
                break

            for i in range(re, rs - 1, -1):
                k=k+1
                matrix[i][cs]=k

            cs += 1

        return matrix