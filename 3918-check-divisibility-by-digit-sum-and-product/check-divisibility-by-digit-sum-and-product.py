class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        pro = 1
        k=n

        while n > 0:
            sum += n % 10
            pro *= n % 10
            n = n / 10
        print(sum,pro)
        return k%(sum + pro)==0
