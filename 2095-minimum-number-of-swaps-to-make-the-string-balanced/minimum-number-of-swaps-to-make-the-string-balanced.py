class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        b=0

        for c in s:
            if c=='[':
             b+=1
            else:
             b-=1
            if b<0:
             m= max(m,-b)
       

        return (m+1)//2
