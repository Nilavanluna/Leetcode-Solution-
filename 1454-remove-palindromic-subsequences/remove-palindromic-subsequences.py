class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        ns=s[::-1]
        if s==ns :
            return 1
        else:
            return 2

        