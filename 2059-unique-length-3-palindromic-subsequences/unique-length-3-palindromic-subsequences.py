class Solution(object):
    def countPalindromicSubsequence(self, s):
        # Record first and last occurrence of each character
        first = [-1] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        ans = 0
        
        # For each character a to z
        for c in range(26):
            if first[c] != -1 and last[c] > first[c]:
                # Look at characters between first and last
                mid_chars = set(s[first[c] + 1 : last[c]])
                ans += len(mid_chars)   # unique middle chars
        
        return ans
