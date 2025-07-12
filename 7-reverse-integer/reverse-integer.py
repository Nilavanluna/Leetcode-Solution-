class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1

        st= str(abs(x))
        s=st[::-1]
        x=int(s)*sign
         
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x