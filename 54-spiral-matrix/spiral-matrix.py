class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # ✅ Corrected: indentation level — moved all the following lines inside the method
        cs = 0
        rs = 0
        re = len(matrix) - 1
        ce = len(matrix[0]) - 1
        l = []

        while True:
            if cs> ce:
                break
            for i in range(cs, ce + 1):
                l.append(matrix[rs][i])  # ✅ rs, not cs

            rs += 1
            if rs > re:
                break

            for j in range(rs, re + 1):
                l.append(matrix[j][ce])

            ce -= 1
            if cs > ce:
                break

            for i in range(ce, cs - 1, -1):
                l.append(matrix[re][i])

            re -= 1
            if rs > re:  # ✅ Optional guard to avoid over-traversing
                break

            for i in range(re, rs - 1, -1):
                l.append(matrix[i][cs])

            cs += 1

        return l
