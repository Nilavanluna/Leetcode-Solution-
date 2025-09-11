class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        groups = []
        count = 1

        # Step 1: Build groups
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # append last run

        # Step 2: Count valid substrings
        for j in range(1, len(groups)):
            res += min(groups[j], groups[j-1])

        return res
