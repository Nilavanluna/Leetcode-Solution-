class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            v=s[i+1:]+s[:i+1]
            
            if v==goal:
              return True
        return False      